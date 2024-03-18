"use client"

import { ADLaM_Display } from "next/font/google";
import Link from "next/link";
import { usePathname } from "next/navigation";

const adlam_display = ADLaM_Display({subsets:["adlam"],weight:"400"})

export function Navbar() {
    const pathname = usePathname()

    return (
    // <div className="fixed top-0 right-0 left-0 z-50">
    <div>
        <div  className="flex justify-center px-[20em] py-5 items-center shadow-md bg-white">
            <h1 className={`${adlam_display.className} text-3xl`}>
            Bezier Curve
            </h1>
        </div>
    </div>
    );
}