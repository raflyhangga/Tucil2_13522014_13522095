"use client"
import { FormEvent, useState } from "react";

export default function FormPoint() {
  const [amountPoints,setAmountPoints] = useState([]);
  const URL = process.env.NEXT_PUBLIC_VERCEL_URL
  ? `https://${process.env.NEXT_PUBLIC_VERCEL_URL}/api`
  : "http://localhost:3000/api";


  function handlePointAmount(event){
    setAmountPoints(Array.from({length: event.target.value}, (_, i) => i + 1))
    console.log(event)
  }

  async function onSubmit(event: FormData) {
    // const formData = new FormData(event.currentTarget)
    console.log("Dikirim!") 
    try{
      const response = await fetch(`${URL}/submit`,{
          method: "POST",
          body:event
      })
      const data = await response.json()
      console.log(data)
    } catch(err){
      console.log(err)
    }
  }



    return (
      <div className="w-[30em]">
        <form action={onSubmit}>
          <div className="flex flex-row gap-5">
            <ul className="flex flex-col">
              <li>
                <label htmlFor="placeholder">Banyak Titik: </label>
              </li>
              <li>
                <input className="border-[3px] rounded-md border-rose-500 px-2 py-[1.5px]" type="number" min={0} max={99} placeholder={`0`} name="banyaktitik" id="placeholder" onChangeCapture={handlePointAmount}/>
              </li>
            </ul>
            <ul className="flex flex-col">
              <li>
                <label htmlFor="iterasi">Iterasi:  </label>
              </li>
              <li>
                <input className="border-[3px] rounded-md border-rose-500 px-2 py-[1.5px]" type="number" min={0} placeholder={`1`} max={99} name="iterasi" id="iterasi"/>
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
                  <input className="border-[3px] rounded-md border-rose-500 px-2 py-[1.5px]" type="number" name={`xpoint`} id="point"/>
                </li>
              </ul>
              <ul className="flex flex-col">
                <li>
                  <label htmlFor={`ypoint`}>Titik Y{key}:  </label>
                </li>
                <li>
                  <input className="border-[3px] rounded-md border-rose-500 px-2 py-[1.5px]" type="number" name={`ypoint`} id="point"/>
                </li>
              </ul>
            </div>))}
            <button type="submit" className="bg-rose-500 px-3 py-2 mt-5 text-white rounded-md">Submit</button>
        </form>
      </div>
    );
}
