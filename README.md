# Lift Equipment API
 This application will contain a library of lifting equipment and exercises that users can access. 

Notes: 
All of the tables and data are from my webscrapper that I coded at {github here}
   Each individual route will have their own table in the data base (type of exercises):
       - /machine?{category searched for}
       - /free-weight?{category searched for}
       - /calisthenics?{category searched for}
       - /endurance?{category searched for}
   Within these routes, the user will be able to search for it by the following categories
       - name of machine
       - muscle being targeted
       - brand of machine
   Along with these searchable variables, the name of the exercise will contain the following information
       - instructions