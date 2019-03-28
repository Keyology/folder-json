import pickle
import pandas
import jsonpickle
import json


# open_pickl_file = open('./weights_matrix.pkl')

# open_pickl_file = open_pickl_file.encode("utf-8").strip()



# convert_to_dict = pickle.load(open_pickl_file)



# convert_to_json = jsonpickle.encode(open_pickl_file)

# create_json_file = open("./matrix.json", "w")

# create_json_file.write(convert_to_json)

# print("***DONE***")

# open_pickl_file.close()

pickle_file = None
with open('weights_matrix.pkl', 'rb') as infile:
    pickle_file = pickle.load(infile)
    with open('100_recs_made_on_keoni.json', 'wb') as outfile:
        json.dump(pickle_file,  outfile)

# convert_to_dict = {}

# with open('./weights_matrix.pkl', 'wb') as outfile:
   
#     # print("***DICT***", convert_to_dict)
#     json.dump(convert_to_dict,  outfile)
#     print('To json file finished.', "Seconds elapsed:", (timer() - time))


