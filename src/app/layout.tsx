import type { Metadata } from "next";
import { Gabarito } from "next/font/google";
import {Navbar} from "@/components/navbar";
import "./globals.css";

const gabarito = Gabarito({subsets:["latin"]})

export const metadata: Metadata = {
  title: "Bezier Curve | Tugas Kecil",
  description: "Bezier Curve simulation",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <Navbar/>
        <div className={`h-screen lg:pt-[150px] pt-[200px] bg-white ${gabarito.className}`}>
          {children}
        </div>
      </body>
    </html>
  );
}
