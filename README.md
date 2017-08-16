# IR-system
An information retrieval system for a comparative analysis of TF-IDF and BM25 ranking mechanisms

## Setting up the repo
* Clone the repo
* Create a new virtual environment using

		virtualenv -p python3 venv
    
* Activate the virtual environement via
		
		source venv/bin/activate
		
* Install the repo requirements via
        
        python setup.py install

* To scrape documents use

        irs scrape        
        
* To create an index use
     
        irs create_index

* To index dumped data use

        irs index_documents $JSON_PATH

* To show results use    
        
        irs run            