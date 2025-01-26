import asyncio
from time import time
import math
import argparse
import json

import aiohttp

from tests.utils import generate_report
from api.database.models import ReportSchema

TEST_API = "http://localhost:5173/api"
TEST_TYPES = ["fire", "flood", "earthquake", "tornado", "hurricane"]


async def send_report(session, report: ReportSchema):
    """Send a report to the backend

    Args:
        session (aiohttp.ClientSession): The aiohttp session
        report (dict): The report data to send
    """
    data = report.model_dump()
    print(data)
    data = json.loads(report.model_dump_json())
    async with session.post(
        f"{TEST_API}/reports/create", json=data
    ) as response:
        if response.status != 200:
            print(f"Failed to create report: {response.status}")


def gauss_pdf(x, mean, deviation):
    """Calculate the pdf of a normal distribution

    Args:
        x (float): the value to calculate the pdf for
        mean (float): the mean of the distribution
        deviation (float): the standard deviation of the distribution
    """
    return (1 / (deviation * math.sqrt(2 * math.pi))) * math.exp(
        -(1 / 2) * (((x - mean) / 2) ** 2)
    )


async def generate_reports(
    report_type,
    lat,
    lon,
    deviation,
    reports_scaler,
    reports_mean_time,
    reports_dev_time,
):
    """Generate and send reports of a specific type at intervals to approximate a normal distribution

    Args:
        report_type (str): The type of report to generate
        lat (float): The latitude coordinate
        lon (float): The longitude coordinate
        deviation (float): The deviation for random coordinates
        reports_scaler (float): How to scale the number of reports that are made
    """
    start_time = time()
    # Make sure that reports come in according to a normal distribution, with a mean time sometime in the future
    time_mean = reports_mean_time + start_time
    async with aiohttp.ClientSession() as session:
        while True:
            report = generate_report(lat, lon, deviation, [report_type])
            await send_report(session, report)
            cur_time = time()
            # Get the number of reports to generate this second (sampling the pdf) and then sleep for the inverse to generate them evenly spaced
            # the number of reports coming into the system, graphed over time, should look like a normal distribution (like how they might in real life)
            to_generate = int(
                gauss_pdf(cur_time, time_mean, reports_dev_time) * reports_scaler
            )
            if to_generate == 0:
                await asyncio.sleep(1)
            else:
                print(f"going to create {to_generate} reports of type {report_type}")
                for _ in range(to_generate):
                    report = generate_report(lat, lon, deviation, [report_type])
                    await send_report(session, report)
                    await asyncio.sleep(1 / to_generate)


async def main():
    """Starts generating reports for a few different types of disasters"""
    parser = argparse.ArgumentParser(prog="Data Injection Test")
    parser.add_argument(
        "-c",
        "--clear",
        action="store_true",
    )
    args = parser.parse_args()
    if args.clear:
        print("clearing db")
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{TEST_API}/reports/clearall") as response:
                if response.status == 200:
                    print("DB cleared")
                else:
                    print(f"Failed to clear db: {response.status}")

    tasks = [
        generate_reports("fire", 0, 0, 1000, 1000, 2, 7),
        generate_reports("flood", 5, 5, 200, 1000, 5, 7),
        generate_reports("earthquake", 0, 0, 50, 1000, 0, 7),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
