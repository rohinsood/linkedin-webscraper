from Excel.ExcelConstants import *

def exporting(namesLi, linksLi, currentCoLi, locationsLi, currentPosLi, experienceLi, educationLi, profCount, searchLink):
    wb = load_workbook("Excel/Template.xlsx")

    ws = wb.active

    ws['B' + str(profCount+1)].value = "Total: " + str(profCount)

    try:
        ws['C' + str(profCount+1)].value = "Search Link: " + shortener.tinyurl.short(searchLink)
    except ShorteningErrorException:
        ws['C' + str(profCount+1)].value = "Search Link " + searchURL

    # iterate over amount of profiles
    for i in range(len(linksLi)):
        # imports names, title, currentCOmpany, locations, and the links 1 person at a time
        row = str(i+3)
        expTempString = ""
        eduTempString = ""
        expStringLi.clear()
        eduStringLi.clear()
        
        ws['B' + row].value = namesLi[i]
        ws['C' + row].value = currentPosLi[i]
        ws['D' + row].value = currentCoLi[i]
        ws['E' + row].value = locationsLi[i]
        tempLinkStr = linksLi[i]

        try:
            ws['H' + row].value = shortener.tinyurl.short(tempLinkStr)
        except ShorteningErrorException:
            ws['H' + row].value = tempLinkStr
        
        # creates a bulleted list for exerpience and edu using for loops to iterate over the different amount of experience members and experience elements that a profile may have
        for z in range(len(experienceLi[i])):
            try:
                tinyURLString = shortener.tinyurl.short(str(experienceLi[i][z][3]))
            except ShorteningErrorException:
                tinyURLString = str(experienceLi[i][z][3])

            expElementString = (" - Position: " + str(experienceLi[i][z][0]) + "\n    - Company: "
            + str(experienceLi[i][z][1]) + "\n    - Duration: " + str(experienceLi[i][z][2]) + 
            "\n    - URL: " + tinyURLString)
        
            expStringLi.append(expElementString)

        print(expStringLi)
        # joins list
        for p in range(len(expStringLi)):
            expTempString = expTempString + "\n" + expStringLi[p]
        
        print(expTempString)
        ws['F' + row].value = expTempString
        expTempString = ""

        for z in range(len(educationLi[i])):
            try:
                tinyURLString = shortener.tinyurl.short(str(educationLi[i][z][3]))
            except ShorteningErrorException:
                tinyURLString = str(educationLi[i][z][3])

            eduElementString = (" - Institution: " + str(educationLi[i][z][0]) + "\n    - Degree: "
                + str(educationLi[i][z][1]) + "\n    - Duration: " + str(educationLi[i][z][2]) + 
                "\n    - URL: " + tinyURLString)

            eduStringLi.append(eduElementString)

        for p in range(len(eduStringLi)):
            eduTempString = eduTempString + eduStringLi[p] + "\n"
        
        # print(eduTempString)
        ws['G' + row].value = eduTempString

    wb.save(downloadsPath + r"/test.xlsx")
