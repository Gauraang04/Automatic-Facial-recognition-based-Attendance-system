import pickle
'''
with open('encodings.pickle', 'rb') as f:
    x = pickle.load(f)
print(x)
'''


with open('encodingsd.pickle', 'rb') as f:
    d = pickle.load(f)
    for key in f:
        print (key)
print(d)


'''

boxes = face_recognition.face_locations(rgb,
		model='hog')


for (i,imagePaths) in enumerate(imagePaths):
    print("[INFO] processing image {}/{}".format(i+1,len(imagePath)))
    name = imagePath.split(os.path.sep)[-2]
    image=cv2.imread(imagePath)
    rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    try:
        boxes=face_recognition.face_locations(rgb,model='cnn')
    except MemoryError:
        boxes=face_recognition.face_locations(rgb,model='hog')
    encodings=face_recognition.face_encodings(rgb,boxes)
    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)

'''



