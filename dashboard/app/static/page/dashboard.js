
const dissolved_minerals = [
    "nitrate",
    "nitrite",
    "ammonia",
    "lead",
    "chlorine",
    "fluoride"
]

const dissolved_minerals_safe_limit = {
    "nitrate"       : [ 0   ,  10 , 'mg/L' ],
    "nitrite"       : [ 0   ,   1 , 'mg/L' ],
    "ammonia"       : [ 0   , 0.5 , 'mg/L' ],
    "lead"          : [ 0   ,  10 , 'ppb'  ],
    "chlorine"      : [ 0.2 ,   4 , 'mg/L' ],
    "fluoride"      : [ 0.7 , 1.2 , 'mg/L' ]
}

function dataRefresh() {

    // let Fetched_data = null

    fetch('/api')
        .then(response => response.json())
        .then(fetched_data => {
            console.log(fetched_data)
            dissolved_minerals.forEach(mineral => {
                var value = fetched_data[mineral]
                var bar = document.querySelector(`#${mineral}`).querySelector(".bar")
                if (dissolved_minerals_safe_limit[mineral][0] <= value && value <= dissolved_minerals_safe_limit[mineral][1]  ) {
                    bar.setAttribute("data-alert", false)
                } else {
                    bar.setAttribute("data-alert", true)
                }
                bar.setAttribute("style", `height: ${ value * 50 / dissolved_minerals_safe_limit[mineral][1] }%;`)
                bar.querySelector(".now_value").textContent = value
                bar.querySelectorAll(".unit").forEach(e => { e.textContent = dissolved_minerals_safe_limit[mineral][2] })
                bar.querySelector(".limit").textContent = `${dissolved_minerals_safe_limit[mineral][0]} - ${dissolved_minerals_safe_limit[mineral][1]}`
            })
        })
}

dataRefresh()

setInterval(dataRefresh, 2000);