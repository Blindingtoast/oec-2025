import * as React from "react"
import { Button } from "@/components/ui/button"
import { BellRing, CirclePlus, Home } from "lucide-react"

const NavDock = () => {
  return (
    <>
      <div className="p-4 flex items-center justify-between w-full">
        <div>
          <a href="/">
            <img src="/logo.png" alt="logo" className="h-8" />
          </a>
        </div>
        <div className="flex gap-2 sm:gap-6 justify-center">
          <a href="/notify-me">
            <Button >
              <BellRing />
              <div className="hidden sm:block">Notify Me</div>
            </Button>
          </a>
          <a href="/">
            <Button >
              <Home />
              <div className="hidden sm:block">Home</div>
            </Button>
          </a>
          <a href="/report/create">
            <Button >
              <CirclePlus />
              <div className="hidden sm:block">Add Disaster</div>
            </Button>
          </a>
        </div>
      </div>
    </>
  )
}



export default NavDock