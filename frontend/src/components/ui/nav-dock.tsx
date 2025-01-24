// make a dock that have 4 bottons, home, notify, and add

import * as React from "react"
import { Button } from "@/components/ui/button"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
import { cn } from "@/lib/utils"
import { BellRing, CirclePlus, Home } from "lucide-react"

export const NavDock = () => {
  return (
    <>
      <div className="flex gap-10 absolute bottom-10 justify-center w-full">

        <Button>
          <BellRing className="h-6 w-6" />
          Notify Me</Button>
        <Button><Home className="h-6 w-6" /> Home</Button>
        <Button><CirclePlus className="h-6 w-6" />
          Add Disaster</Button>
      </div>
    </>
  )
}

export default NavDock