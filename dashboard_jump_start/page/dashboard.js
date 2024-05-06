
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

    const apt_route = 'http://127.0.0.1:8002/api';
    const options = {
        method: 'GET',
        headers: {
            'Origin': 'http://localhost:5500' // Add this if necessary
        }
    };

    fetch(apt_route, options)
        .then(response => response.json())
        .then(fetched_data => {
            console.log(fetched_data);
        });
}

dataRefresh()

setInterval(dataRefresh, 2000);