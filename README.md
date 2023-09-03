 
 ## Hydralit Examples<img src="https://github.com/TangleSpace/hydralit/raw/main/docs/images/hydra.png" alt="drawing" width="50"/>
## [Hydralit package](https://github.com/TangleSpace/hydralit) is a wrapping and template project to combine multiple independant (or somewhat dependant) Streamlit applications into a multi-page application.

Currently the project implements a host application HydraApp and each child application simply needs to be a class deriving from the HydraHeadApp class and implement a single, simple method, run().

This is a sample project that tries to show some of the potential of using the Hydralit package to create multi-page Streamlit applications using the existing approach of creating a number of single applications and then using this package to make it easy to create a multi-page application from the individual applications in a simple way.

The ability to add as many applications as you wish and create a dedicated secure login application to front door all the seperate applications, means you can think about your project code and just add it to the host Hydralit application and you have a full-blooded, state aware multi-page application, with security and navigation.

If you find this project useful, please give it a star or atleast a "hey! i find this useful, thanks" callout, I hope to make everyones life alittle easier by using Hydralit.

### You can try it out by installing the project requirements and then running the sample secure app as below.

##### First install the project dependencies using the requirements.txt file, then let rip as below.
```bash
pip install -r requirements.txt
```

## Installation
Hydralit can be installed from PyPI:

```bash
pip install hydralit
```

You can run the sample secure app with the commands below. (dummy login details are, u:joe, p:joe).

```bash
hydralit_example> streamlit run secure_app.py
```

<h1><a href="https://hydralit-secure-sample.herokuapp.com/">You can see this example running here</a></h1>
<img src="https://github.com/TangleSpace/hydralit-example/raw/main/docs/images/hydralit-secure-example.gif" alt="example" width="80%"/>

The host application code is shown below as an example of how such a multi-page application with authentication and lots of bells and whistles can be created with very little code, yet alot of configuration potential.


#   d e n t a l S c a n n i n g  
 #   D e n t a l S c a n n i n g  
 #   D e n t a l S c a n n i n g  
 #   D e n t a l S c a n n i n g  
 #   D e n t a l S c a n n i n g  
 