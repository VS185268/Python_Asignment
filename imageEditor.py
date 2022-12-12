from PIL import Image,ImageEnhance,ImageFilter
import os
fold_new='imgs' #images folder which we have to pass
fold_edited='editedimgs'#edited images folder
All_imgs=os.listdir(fold_new) #getting list of files in the given folder
for each in All_imgs:
    # opening each file as the image 
    img=Image.open(f"{fold_new}/{each}")
    # By adjusting this factor we can vary the Contrasting level
    effecting_Factor=0.8
    enhancer=ImageEnhance.Contrast(img)
    edit=enhancer.enhance(effecting_Factor)
    #getting first name of the files which are present in the folder
    new_name=os.fold_new.splitdata(each)[0]
    #finally we saved the edited file in the new folder
    edit.save(f'{fold_edited}/{new_name}_edited.jpg')
#Here print statement is for knowing the successful termination
print("Here successfully we edited the files")    
    
