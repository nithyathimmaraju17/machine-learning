#make predictions on some new data


new_data = [(720,4,1), (300,2,3) , (400,3,4) ]

#conv to numpy arr
new_array = np.asarray(new_data)

#o/p labels
labels=["reject","admit"]

#make pred
prediction=model.predict(new_array)

#get no of test cases used
no_of_test_cases, cols = new_array.shape

#res
for i in range(no_of_test_cases):
	print("Status of Student with GRE scores = {}, GPA grade = {}, Rank = {} will be ----- {}".format(new_data[i][0],new_data[i][1],new_data[i][2], labels[int(prediction[i])]))
    print('#--------------END------THANKS-------------#')