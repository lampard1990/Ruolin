#Read data from spreasheet
import openpyxl,pprint

wb=openpyxl.load_workbook('censuspopdata.xlsx')
sheet=wb['Population by Census Tract']
countyData = {}


for row in range(2,sheet.max_row+1):
    #each row in the spreasheet has data for one census tract
    state=sheet['B'+str(row)].value
    county=sheet['C'+str(row)].value
    pop=sheet['D'+str(row)].value

    #make sure the key for this state exists
    countyData.setdefault(state, {})
    #make sure the key for this couty in this state exsits
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    #each row represetns one census tract, so increment by one
    countyData[state][county]['tracts']+=1

    #increase the county pop by the pop in this census tract
    countyData[state][county]['pop']+=int(pop)

    
resultfile=open('census2010.txt','w')
resultfile.write('all date= '+pprint.pformat(countyData))
resultfile.close()
