#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Kris Czaja, 2021-Nov-12, Altered code to use dictionairies
# Kris Czaja, 2021-Nov-13, Testing, debugging
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
dicRow = {} # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# Get user Input


print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()


    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        
        print ('\n')
        print ('Following entries were loaded from ', strFileName, ': ')
        
        lstRow = []
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            strID = lstRow[0]
            strTitle = lstRow[1]
            strArtist = lstRow[2]
            dicRow = {'ID': strID, 'Title': strTitle, 'Artist': strArtist }
            lstTbl.append(dicRow)
            print(lstRow)
        objFile.close
        
        print ('\n')
        pass
       
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        
        print ('\n')
        
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': strID, 'Title': strTitle, 'Artist': strArtist }
        lstTbl.append(dicRow)
   
    
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        
        print ('\n')
        
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ',')

    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        
        print ('\n')
        
        IDDel = input('Enter ID of CD you want to delete:  ' )

        for row in lstTbl:
            if row['ID'] == IDDel:
                print ('Entry: ', *row.values(), 'was deleted.' , '\n')
                print ('Save Inventory to reflect these changes in the text file', '\n')
                lstTbl.remove(row)

            else:
                pass
            
    
  
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        
        print ('\n')
        
        print('you saved: ')
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            dicRow = ''
            for key, value in row.items():
                dicRow += str(value) + ','
            dicRow = dicRow[:-1] + '\n'
            objFile.write(dicRow)
            print(dicRow )
        objFile.close()
        
    
    
    
    else:
        print('Please choose either l, a, i, d, s or x!')

