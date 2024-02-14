import random

def rand():
    return random.randint(90, 130) / 100


def DashboardData():
    return {
        # "ph"            : round(7.2 * rand() , 1 ),
        # "tds"           : round(487 * rand() , 1 ),
        # "turbidity"     : round(4.8 * rand() , 1 ),
        # "salinity"      : round(1.5 * rand() , 1 ),
        "nitrate"       : round(9.2 * rand() , 1 ),
        "nitrite"       : round(0.9 * rand() , 1 ),
        "ammonia"       : round(0.3 * rand() , 1 ),
        "lead"          : round(8 * rand() , 1 ),
        "chlorine"      : round(3 * rand() , 1 ),
        "fluoride"      : round(0.8 * rand() , 1 )
    }