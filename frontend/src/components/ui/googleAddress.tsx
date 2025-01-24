// use the code above to create a component that allows a user to type in an adress and select the adress from google maps api
// then use the address to populate the form fields

import React, { useRef, useEffect } from "react"
import { useFormContext } from "react-hook-form"
import { useDebouncedCallback } from "use-debounce"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"


export const GoogleAddress = () => {
  const { register, setValue } = useFormContext()
  const inputRef = useRef<HTMLInputElement>(null)
  const [debouncedCallback] = useDebouncedCallback((value: string) => {
    setValue("address", value)
  }, 500)

  useEffect(() => {
    const input = inputRef.current
    if (!input) return

    const autocomplete = new google.maps.places.Autocomplete(input, {
      types: ["geocode"],
      componentRestrictions: { country: "us" },
    })

    autocomplete.addListener("place_changed", () => {
      const place = autocomplete.getPlace()
      debouncedCallback(place.formatted_address)
    })

    return () => {
      google.maps.event.clearInstanceListeners(input)
    }
  }, [debouncedCallback, setValue])

  return (
    <div>
      <Input
        ref={inputRef}
        name="address"
        placeholder="Enter your address"
        {...register("address")}
      />
      <Button type="button">Use my current location</Button>
    </div>
  )
}
