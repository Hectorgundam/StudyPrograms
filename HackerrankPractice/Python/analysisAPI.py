# Incomplete

# API Analysis
# Python program

# there are several interdependent resources being served from "https://api.example.com" where each resource is parameterized with some id. 
# For example, the API "https://api.example.com/resource1/id1/resource2/id2/resource3/id3" serves the resource "resource1/resource2/resource3? and is said to have 3-level dependency

# Given n strings as an array, requests, list the resources served with single-level dependency, followed by two-level dependency, followed by 3-level dependency, and so on
# Each level of resources should be in lexicographically sorted order e.g. resource1 precedes resource10 which precedes resource 2
# Note that each of the served resources has the form "resource<id>" 

# Example 
# Suppose n=4 and requests=["https://api.example.com/resource2/id/resource3/id2", "https://api.example.com/resource3", "https://api.example.com/resource2", "https://api.example.com/resource1/id/resource3/id2"]

# Here the resource being served are "resource2/resource3", "resource", "resource2" and "resource1/resource3" respectively 
# Hence the answer in the desired format will be ["resource2", "resource3", "resource1/resource3", "resource2/resource3"]

# Function description
# Complete the function getResourceList in the editor 
# getResouceList has the following parameters 
# string request[n] that is an array of strings 

# Returns 
# string[] that is a list of resources 

# Constraints
# 1 <= n <= 10^4
# 1<= l request[i] l <= 90

# Code in python

import math
import os
import random
import re
import sys


def getResourceList(requests):

    # Test printing the contents of request 
    # print(requests)

    # Need to store resources in a dictionary 
    resourceDictionary = {}

    # Cycling through the elements in requests 
    for request in requests: 

        # Variable resources will contain the resources# after the first section is trimmed and split by / 
        # This will leave us with the resources name 
        # Considering alternate elements since the ids are interspersed
        resources = request.replace("https://api.example.com/", "").split("/")[::2]

        # Test printing the contents of resources 
        # print("The contents of resources are ", resources)

        # Variable depth will be equal to the lenght of our resources list 
        depth = len(resources)

        # Test printing the contents of depth
        # print("The contents of depth are ", depth)

        # Converting our list of resources into a string 
        resourceString = '/'.join(resources)

        # Test printing the contents of resourceString
        # print("The contents of resourceString are ", resourceString)


        if depth not in resourceDictionary: 

            resourceDictionary[depth] = set()

        resourceDictionary[depth].add(resourceString)

        # Testing printing the contents of resourceDictionary 
        # print("The contents of resourceDictionary are ", resourceDictionary)

    # Now we sort the resources lexicographically

    # Need a list to store the resources once they are sorted 
    sortedResources = []

    for depth in sorted(resourceDictionary.keys()): 

        sorted_set = sorted(resourceDictionary[depth], key=lambda x: [int(re.search(r'(\d+)', r).group(1)) if re.search(r'(\d+)', r) else r for r in x.split('/')])

        sortedResources.extend(sorted_set)

    return sortedResources

if __name__ == '__main__':
    
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # requests_count = int(input().strip())

    # requests = []

    requests = [
        "https://api.example.com/resource2/id/resource3/id2",
        "https://api.example.com/resource3",
        "https://api.example.com/resource2",
        "https://api.example.com/resource1/id/resource3/id2"
    ]


    # for _ in range(requests_count):
        
        # requests_item = input()
        
        # requests.append(requests_item)

    result = getResourceList(requests)

    for r in result: 

        print(r)

    # fptr.write('\n'.join(result))
    
    # fptr.write('\n')

    # fptr.close()

