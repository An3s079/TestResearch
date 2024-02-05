import docx2txt
import glob
import os
crime_type = ["Harmful White Collar", "Harmful Street", "Financial White Collar", "Financial Street"]

for crime in crime_type:
    directory = glob.glob('C:\\Users\\an3sf\\OneDrive\\Documents\\GitHub\\STS-Project\\News Articles\\'+crime+'\\*.docx')
    for file_name in directory:
        with open(file_name, 'rb') as infile:
            with open(file_name[:-5]+'.txt', 'w', encoding='utf-8') as outfile:
                doc = docx2txt.process(infile)
                outfile.write(doc)
        os.remove(file_name)
    

print("=========")
print("All done!")
