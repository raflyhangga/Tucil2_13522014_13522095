"use client"
import FormPoint from "@/components/formpoint";
import { LineChart } from "@/components/linechart";
import { Suspense, useState } from 'react'


export default function Home() {
  const [x,setX] = useState([0]);
  const [y,setY] = useState([0]);
  const [ctrlX,setCtrlX] = useState([0])
  const [ctrlY,setCtrlY] = useState([0])
  const [execTime,setExecTime] = useState(0)


  function onSubmit(listX:number[],listY:number[],ctrlX:number[],ctrlY:number[],execTime:number){
    setX([ctrlX[0],...listX,ctrlX[ctrlX.length-1]])
    setY([ctrlY[0],...listY,ctrlY[ctrlY.length-1]])
    setCtrlX(ctrlX)
    setCtrlY(ctrlY)
    setExecTime(execTime)
  }


  return (
    <div>
      <div className="flex flex-col flex-wrap lg:flex-row justify-center gap-10 items-center mx-10">
        <FormPoint onSubmit={onSubmit}/>
        <div className="shadow-md md:w-[1000px] w-[100vw] ">
          <Suspense fallback={<p>Loading....</p>}>
            <LineChart
              xScatter={ctrlX}
              yScatter={ctrlY}
              xValues={x}
              yValues={y}
            />
            <span className="ml-2">Execution Time: {execTime} ms</span>
          </Suspense>
        </div>
      </div>
    </div>
  );
}
