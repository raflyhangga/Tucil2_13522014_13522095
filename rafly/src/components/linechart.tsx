import CanvasJSReact from '@canvasjs/react-charts';

var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;


export function LineChart({xValues, yValues,xScatter,yScatter}:number[])  {
    let arr_of_scatter = []
    let arr_of_lines = []
    for(let i=0;i<xScatter.length;i++){
        arr_of_scatter.push({
            x:xScatter[i],
            y:yScatter[i]
        })
    }

    for(let i=0;i<xValues.length;i++){
        arr_of_lines.push({
            x:xValues[i],
            y:yValues[i]
        })
    }

    const options = {
        data: [
            {
                type: "line",
                dataPoints: arr_of_lines
            },
            {
                type: "scatter",
                dataPoints: arr_of_scatter
            },

        ],
        axisX:{
            gridThickness: 0,
            tickLength: 0,
            lineThickness: 0,
            labelFormatter: function(){
              return " ";
            }
          },
          axisY:{
            gridThickness: 0,
            tickLength: 0,
            lineThickness: 0,
            labelFormatter: function(){
              return " ";
            }
        },
        options: {
            responsive:true
        }
    }

return <CanvasJSChart options = {options} className="h-full" />;
};