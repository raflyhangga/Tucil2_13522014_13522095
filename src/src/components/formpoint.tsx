"use client"
import { Switch } from "./ui/switch";
import { ChangeEvent, FormEvent, useState } from "react";
import { Button } from "./ui/button";
import { Label } from "./ui/label";

type submitFunction = (listX:number[],listY:number[],ctrlX:number[],ctrlY:number[],execTime:number) => void;

export default function FormPoint({onSubmit}:{onSubmit:submitFunction}) {
  const [amountPoints,setAmountPoints] = useState([0,1,2]);
  const [isBrute,setBrute] = useState(false)
  const URL = process.env.NEXT_PUBLIC_VERCEL_URL
  ? `https://${process.env.NEXT_PUBLIC_VERCEL_URL}/api`
  : "http://localhost:3000/api";
  const ENDPOINT = isBrute? `${URL}/submitbrute`:`${URL}/submitdnc`

  function handlePointAmount(event:ChangeEvent<HTMLInputElement>){
    const numberOfPoints = parseInt(event.target.value,10)

    setAmountPoints(Array.from({length: numberOfPoints}, (_, i) => i + 1))
    console.log(event)
  }

  function changeSolveMode(){
    const currentState = isBrute
    setBrute(!currentState)
  }

  async function submitHandler(event: FormData): Promise<void> {
    console.log("Dikirim!") 
    try{
      const response = await fetch(ENDPOINT,{
          method: "POST",
          body:event
      })
      const data = await response.json()
      console.log(data)

      const file = event.get('documents[]') as string
      const xpointValues =  Array.from(event.getAll('xpoint'), x => x.toString());
      const ypointValues =  Array.from(event.getAll('ypoint'), x => x.toString());
      onSubmit(
        data.poinX,data.poinY,
        xpointValues.map(x=>parseFloat(x)),
        ypointValues.map(x=>parseFloat(x)),
        data.executionTime
      )
    } catch(err){
      console.log(err)
    }
  }



    return (
      <div className="w-[30em] mx-10">
        <form action={submitHandler}>
          <div className="flex flex-row gap-5">
            <ul className="flex flex-col">
              <li>
                <label htmlFor="placeholder">Banyak Titik: </label>
              </li>
              <li>
                <input className="border-[3px] rounded-md border-rose-500 px-2 py-[1.5px]" type="number" min={3} max={99} required placeholder={`3`} name="banyaktitik" id="placeholder" onChangeCapture={handlePointAmount}/>
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
                  <input className="border-[3px] rounded-md border-rose-500 px-2 py-[1.5px]" placeholder={`${Math.floor((Math.random() * 100) + 1)}`} required type="number" step="any" name={`xpoint`}/>
                </li>
              </ul>
              <ul className="flex flex-col">
                <li>
                  <label htmlFor={`ypoint`}>Titik Y{key}:  </label>
                </li>
                <li>
                  <input className="border-[3px] rounded-md border-rose-500 px-2 py-[1.5px]" placeholder={`${Math.floor((Math.random() * 100) + 1)}`} required type="number" step="any" name={`ypoint`}/>
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