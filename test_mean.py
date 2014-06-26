from mean_sightings import get_sightings 

filename= "sightings_tab_sm.csv"
def test_water_is_corrrect():
    watrec,watmean = get_sightings(filename,"Water")
    assert watrec==2, "number of records for water is wrong"
    assert watmean==17, "water mean is wrong"


def test_clay_is_corrrect():
    clayrec,claymean = get_sightings(filename,"Clay")
    assert clayrec==2, "number of records for clay is wrong"
    assert claymean==25.5, "clay mean is wrong"



def test_not_present():
    norec,nomean = get_sightings(filename, "not present")
    assert norec==0, "Biosig not present"
    assert nomean ==0, "mean is not present"

