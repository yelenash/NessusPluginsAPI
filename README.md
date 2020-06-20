# NessusPluginsAPI
start elasticsearch docker:
```
   docker pull docker.elastic.co/elasticsearch/elasticsearch:7.5.2 
 ``` 
 ```
   docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.5.2
 ```
 run data clone: https://github.com/yelenash/nessusDataClone
 
 
 
 
 ### execute:
  
 ```
 pip install -r requirements.txt
 ``` 
 
```
 python  wsgi.py 
``` 
 
```
 http://localhost:5000/
``` 

### tests:
   
```
 pytest
``` 

