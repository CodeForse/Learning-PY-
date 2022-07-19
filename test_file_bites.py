file=open('tmp.txt','r+')
# print(file.seek(file.read().find('[')+1)) # excludes [
# print(file.read())

# print(file.read()+'\n\n\n\n')
# file.seek(0)
# print(file.read()+'\nDONE')
# tmptext=file.readlines()

te = [
      {
        "Name": "Bala",
        "phone": "None"
      },
      {
        "Name": "Bala",
        "phone": "None"
      },
      {
        "Name": "Bala",
        "phone": "None"
      },
      {
        "Name": "Bala",
        "phone": "None"
      },
      {
          "Name": "Bala1",
          "phone": "None"
      }      
    ]

unique = { each['Name'] : each for each in te }#if each['Name'] == 'Bala1'
#similiar to filter list(filter(None, f.read().split('\n')))
#my_dict = {k: ' '.join(v) for k,v in tmp_dict.items()} to склеить элементы листа по пробелам

print(unique.values())




