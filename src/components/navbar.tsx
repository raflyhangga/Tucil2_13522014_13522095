"use client"

import { ADLaM_Display } from "next/font/google";
import Link from "next/link";
import { usePathname } from "next/navigation";

const adlam_display = ADLaM_Display({subsets:["adlam"],weight:"400"})

export function Navbar() {
    const pathname = usePathname()

    return (
    <div className="fixed top-0 right-0 left-0 z-50">
        <div  className="flex lg:flex-row flex-col justify-between px-[20em] py-5 items-center shadow-md bg-white">
            <h1 className={`${adlam_display.className} text-3xl`}>
            Bezier Curve
            </h1>

            <div>
            <ul className="flex lg:flex-row flex-col lg:gap-10 font-semibold lg:text-xl md:text-md text-center">
                <li className={`hover:scale-105 hover:text-orange-400 hover:cursor-pointer`}>
                <Link className={`${pathname == "/"? "text-red-400":""} `} href="/">Divide & Conquer</Link>
                </li>
                <li className="hover:scale-105 hover:text-orange-400 hover:cursor-pointer">
                <Link className={`${pathname == "/bruteforce"? "text-red-400":""} `} href="/bruteforce">Brute Force</Link>
                </li>
            </ul>
        </div>
        </div>
    </div>
    );
}