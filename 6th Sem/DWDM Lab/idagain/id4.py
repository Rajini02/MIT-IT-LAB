import pandas as pd #for manipulating the csv data
import numpy as np #for mathematical calculation
data_m = pd.read_csv("/Users/PRANAV/Desktop/VI sem/dwdm lab/idagain/id4_d.csv") #importing the dataset from the disk

data_m.head() #viewing some row of the dataset

#finding info gain
def calc_total_entropy(data, label, class_list):
    total_row = data.shape[0]
    total_entr = 0
    
    for c in class_list: #for each class in the label
        total_class_count = data[data[label] == c].shape[0]
        total_class_entr = - (total_class_count/total_row)*np.log2(total_class_count/total_row)
        total_entr += total_class_entr
    
    return total_entr

#for each label class in attribute classes
def calc_entropy(att_value_data, label, class_list):
    class_count = att_value_data.shape[0]
    entropy = 0
    
    for c in class_list:
        label_class_count = att_value_data[att_value_data[label] == c].shape[0]
        entropy_class = 0
        if label_class_count != 0:
            probability_class = label_class_count/class_count #probability of the class
            entropy_class = - probability_class * np.log2(probability_class)  #entropy
        entropy += entropy_class
    return entropy

#for each class in an attribute
def calc_info_gain(att_name, data, label, class_list):
    att_value_list = data[att_name].unique()
    #print(att_value_list)
    total_row = data.shape[0]
    #print(total_row)
    att_info = 0.0
    
    for att_value in att_value_list:
        att_value_data = data[data[att_name] == att_value]
        #print(att_value_data)
        att_value_count = att_value_data.shape[0]
        #print(att_value_count)
        att_value_entropy = calc_entropy(att_value_data, label, class_list)
        att_value_probability = att_value_count/total_row
        att_info += att_value_probability * att_value_entropy
        
    return calc_total_entropy(data, label, class_list) - att_info #calculating information gain by subtracting

# finds max info gain amongst attributes
def find_most_informative_att(data, label, class_list):
    att_list = data.columns.drop(label) #N.B. label is not a att, so dropping it
    max_info_gain = -1
    max_info_att = None
    
    for att in att_list:  #for each att in the dataset
        #print(att)
        att_info_gain = calc_info_gain(att, data, label, class_list)
        if max_info_gain < att_info_gain:
            max_info_gain = att_info_gain
            max_info_att = att
            
    return max_info_att

def generate_sub_tree(att_name, data, label, class_list):
    att_value_count_dict = data[att_name].value_counts(sort=False)
    #print(att_value_count_dict)
    tree = {}
    
    for att_value, count in att_value_count_dict.items():
        att_value_data = data[data[att_name] == att_value]
        #print(att_value_data)
        assigned_to_node = False
        for c in class_list: #for each class
            class_count = att_value_data[att_value_data[label] == c].shape[0] #count of class c

            if class_count == count:
                tree[att_value] = c #adding node to the tree
                data = data[data[att_name] != att_value]
                assigned_to_node = True
        if not assigned_to_node: #not pure class
            tree[att_value] = "?" #as att_value is not a pure class, it should be expanded further, 
                                    
            
    return tree, data


def make_tree(root, prev_att_value, data, label, class_list):
    if data.shape[0] != 0: #if dataset becomes enpty after updating
        max_info_att = find_most_informative_att(data, label, class_list)
        tree, data = generate_sub_tree(max_info_att, data, label, class_list)
        next_root = None
        
        if prev_att_value != None: #add to middle node of the tree
            root[prev_att_value] = dict()
            root[prev_att_value][max_info_att] = tree
            next_root = root[prev_att_value][max_info_att]
        else: #add to root of the tree
            root[max_info_att] = tree
            next_root = root[max_info_att]
        
        for node, branch in list(next_root.items()): #iterating the tree node
            if branch == "?": #if it is expandable
                att_value_data = data[data[max_info_att] == node]
                make_tree(next_root, node, att_value_data, label, class_list)


def id3(data_m, label):
    data = data_m.copy()
    tree = {}
    class_list = data[label].unique()
    #print(class_list)
    make_tree(tree, None, data, label, class_list)
    return tree

tree = id3(data_m, 'Play Tennis')
print(tree)