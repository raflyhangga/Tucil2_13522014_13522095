"use client"
import FormPoint from "@/components/formpoint";
import { Suspense, useState } from 'react'
import Plot from 'react-plotly.js'

export default function Home() {
  const [x,setX] = useState([1,2,7]);
  const [y,setY] = useState([2,6,3]);


  return (
    <div>
      <div className="flex flex-col flex-wrap lg:flex-row justify-center gap-10 items-center">
        <FormPoint/>
        <div className="shadow-md md:w-[1000px] md:h-[600px] w-[100vw] h-[60px]">
          <Suspense fallback={<p>Loading....</p>}>
            <Plot
              data={[
                {
                  x,
                  y,
                  type: 'scatter',
                  mode: 'lines+markers',
                  marker: {color: 'red'},
                },
              ]}
              // config={{responsive:"true"}}
              className="w-full h-full"
            />
          </Suspense>
        </div>
      </div>
    </div>
  );
}
