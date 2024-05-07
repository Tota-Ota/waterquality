const raw_parameters = [
    "pH",
    "Turbidity",
    "Temperature",
]

const predicted_parameters = [
    "Hardness",
    "Solids",
    "Chloramines",
    "Sulfate",
    "Conductivity",
    "Organic_carbon",
    "Trihalomethanes",
    "Turbidity",
    "Potability",
]

const parameter_data_sheet = {

    "pH"                    : [10   , ""    ],
    "Turbidity"             : [1    , "NTU" ],
    "Temperature"           : [100  , "°C"  ],

    "Hardness"              : [7    , "mg/L"],
    "Solids"                : [7    , "ppm" ],
    "Chloramines"           : [7    , "ppm" ],
    "Sulfate"               : [7    , "mg/L"],
    "Conductivity"          : [7    , "S/cm"],
    "Organic_carbon"        : [7    , "ppm" ],
    "Trihalomethanes"       : [7    , "g/L" ],
    "Turbidity"             : [7    , "NTU" ],
    "Potability"            : [0    , ""    ],

}

function dataRefresh() {

    fetch('/api')
        .then(response => response.json())
        .then(fetched_data => {

            // timestamp

            timestamp = fetched_data.timestamp

            document.querySelector('#date').textContent = timestamp.split("T")[0]
            document.querySelector('#time').textContent = timestamp.split("T")[1].split(".")[0]

            // cards

            raw_parameters.forEach(parameter => {

                const value = fetched_data['raw-data'][parameter]

                document.querySelector(`#${parameter}`).textContent = value

                card = document.querySelector(`.card:has(#${parameter})`)

                if ( value >= parameter_data_sheet[parameter][0] ) {
                    card.setAttribute("data-alert", true)
                } else {
                    card.setAttribute("data-alert", false)
                }
                
                document.querySelector(`.card:has(#${parameter}) .units`).textContent = parameter_data_sheet[parameter][1]

                document.querySelector(`.card:has(#${parameter}) .safe-limit span`).textContent = `${parameter_data_sheet[parameter][0]} ${parameter_data_sheet[parameter][1]}`

            })

            // bar graph

            predicted_parameters.forEach(parameter => {

                const value = fetched_data['processed'][parameter]

                const bar = document.querySelector(`#${parameter} .bar`)

                bar.setAttribute("style", `height: ${value * 50 / parameter_data_sheet[parameter][0]}%;`)

                if ( value >= parameter_data_sheet[parameter][0] ) {
                    bar.setAttribute("data-alert", true)
                } else {
                    bar.setAttribute("data-alert", false)
                }

                bar.querySelector(".now_value").textContent = value

                bar.querySelector(".limit").textContent = `${parameter_data_sheet[parameter][0]} ${parameter_data_sheet[parameter][1]}`

                bar.querySelector(".unit").textContent = parameter_data_sheet[parameter][1]

            })

            // dissolved_minerals.forEach(mineral => {
            //     var value = fetched_data[mineral]
            //     var bar = document.querySelector(`#${mineral}`).querySelector(".bar")
            //     if (dissolved_minerals_safe_limit[mineral][0] <= value && value <= dissolved_minerals_safe_limit[mineral][1]  ) {
            //         bar.setAttribute("data-alert", false)
            //     } else {
            //         bar.setAttribute("data-alert", true)
            //     }
            //     bar.setAttribute("style", `height: ${ value * 50 / dissolved_minerals_safe_limit[mineral][1] }%;`)
            //     bar.querySelector(".now_value").textContent = value
            //     bar.querySelectorAll(".unit").forEach(e => { e.textContent = dissolved_minerals_safe_limit[mineral][2] })
            //     bar.querySelector(".limit").textContent = `${dissolved_minerals_safe_limit[mineral][0]} - ${dissolved_minerals_safe_limit[mineral][1]}`
            // })
        })
}

dataRefresh()

// setInterval(dataRefresh, 2000);