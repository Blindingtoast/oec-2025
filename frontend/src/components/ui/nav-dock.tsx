import * as React from "react"
import { Button } from "@/components/ui/button"
import { BellRing, CirclePlus, Home } from "lucide-react"

const NavBar = () => {
  return (
    <>
      <div className="p-4 flex items-center justify-between w-full">
        <div>
          CANotify
        </div>
        <div className="flex gap-6 justify-center">
          <a href="/notify-me">
            <Button >
              <BellRing />
              Notify Me
            </Button>
          </a>
          <a href="/">
            <Button >
              <Home />
              Home
            </Button>
          </a>
          <a href="/report/create">
            <Button >
              <CirclePlus />
              Add Disaster
            </Button>
          </a>
        </div>
      </div>
    </>
  )
}



export default NavBar