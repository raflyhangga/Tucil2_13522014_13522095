"use client"
import { Switch } from "./ui/switch";
import { FormEvent, useState } from "react";
import { Button } from "./ui/button";
import { Label } from "./ui/label";

export default function FormPoint({onSubmit}) {
  const [amountPoints,setAmountPoints] = useState([]);
  const [isBrute,setBrute] = useState(false)
  const URL = process.env.NEXT_PUBLIC_VERCEL_URL
  ? `https://${process.env.NEXT_PUBLIC_VERCEL_URL}/api`
  : "http://localhost:3000/api";
  const ENDPOINT = isBrute? `${URL}/submitbrute`:`${URL}/submitdnc`

  function handlePointAmount(event){
    setAmountPoints(Array.from({length: event.target.value}, (_, i) => i + 1))
    console.log(event)
  }

  function changeSolveMode(){
    const currentState = isBrute
    setBrute(!currentState)
  }

  async function submitHandler(event: FormData) {
    // const formData = new FormData(event.currentTarget)
    console.log("Dikirim!") 
    try{
      const response = await fetch(ENDPOINT,{
          method: "POST",
          body:event
      })
      const data = await response.json()
      console.log(data)
      onSubmit(data.poinX,data.poinY,event.getAll('xpoint').map(x=>parseFloat(x)),event.getAll('ypoint').map(x=>parseFloat(x)),data.executionTime)
    } catch(err){
      console.log(err)
    }
  }



    return (
      <div className="w-[30em]">
        <form action={submitHandler}>
          <div className="flex flex-row gap-5">
            <ul className="flex flex-col">
              <li>
                <label htmlFor="placeholder">Banyak Titik: </label>
              </li>
              <li>
                <input className="border-[3px] rounded-md border-rose-500 px-2 py-[1.5px]" type="number" min={3} max={99} required placeholder={`0`} name="banyaktitik" id="placeholder" onChangeCapture={handlePointAmount}/>
              </li>
            </ul>
            <ul className="flex flex-col">
              <li>
                <label htmlFor="iterasi">Iterasi:  </label>
              </li>
              <li>
                <input className="border-[3px] rounded-md border-rose-500 px-2 py-[1.5px]" type="number" min={1} required placeholder={`1`} max={99} name="iterasi" id="iterasi"/>
              </li>
            </ul>
          </div>
          {amountPoints.map((_,key) => (
            <div key={key} className="flex flex-row gap-5 mt-4">
              <ul className="flex flex-col">
                <li>
                  <label htmlFor={`xpoint`}>Titik X{key}: </label>
                </li>
                <li>
                  <input className="border-[3px] rounded-md border-rose-500 px-2 py-[1.5px]" required type="number" step="any" name={`xpoint`} id="point"/>
                </li>
              </ul>
              <ul className="flex flex-col">
                <li>
                  <label htmlFor={`ypoint`}>Titik Y{key}:  </label>
                </li>
                <li>
                  <input className="border-[3px] rounded-md border-rose-500 px-2 py-[1.5px]" required type="number" step="any" name={`ypoint`} id="point"/>
                </li>
              </ul>
            </div>))}
            <div className="flex items-center mt-2">
              <button type="submit" className="bg-rose-500 px-3 py-2 text-white rounded-md">Submit</button>
              <div className="flex items-center space-x-2 ml-5">
                <Switch id="solve-mode" checked={isBrute} onCheckedChange={changeSolveMode} />
                {isBrute && <Label htmlFor="solve-mode">Brute Force</Label>}
                {!isBrute && <Label htmlFor="solve-mode">Divide & Conquer</Label>}
              </div>
            </div>
        </form>
      </div>
    );
}
