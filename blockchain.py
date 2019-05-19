# Module 1 - Create a Blockchain

# To be installed:
# Flask==0.12.2: pip install Flask==0.12.2
# Postman HTTP Client: https://www.getpostman.com/

# Importing the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

# Part 1 - Building a Blockchain

class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]	<!DOCTYPE html>
	<html lang="zxx" class="no-js">
	<head>
		
		<!-- Mobile Specific Meta -->
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<!-- Favicon-->
		<link rel="shortcut icon" href="img/fav.png">
		<!-- Author Meta -->
		<meta name="author" content="codepixer">
		<!-- Meta Description -->
		<meta name="description" content="">
		<!-- Meta Keyword -->
		<meta name="keywords" content="">
		<!-- meta character set -->
		<meta charset="UTF-8">
		<!-- Site Title -->
		<title>Blockchain</title>

		<link href="https://fonts.googleapis.com/css?family=Poppins:100,200,400,300,500,600,700" rel="stylesheet"> 
			<link rel="stylesheet" href="css/font-awesome.min.css">
			<link rel="stylesheet" href="css/bootstrap.css">
			<link rel="stylesheet" href="css/magnific-popup.css">
			<link rel="stylesheet" href="css/nice-select.css">					
			<link rel="stylesheet" href="css/animate.min.css">
			<link rel="stylesheet" href="css/owl.carousel.css">
			<link rel="stylesheet" href="css/main.css">
		</head>
		<body>

			  <header id="header" id="home">
			    <div class="container">
			    	<div class="row align-items-center justify-content-between d-flex">
				      <div id="logo">
				        <a href="index.html"><img src="img/logo.png" alt="" title="" /></a>
				      </div>
				      <nav id="nav-menu-container">
				        <ul class="nav-menu">
				          <li class="menu-active"><a href="#home">Home</a></li>
				          <li><a href="#add">Add Block</a></li>
				          <li><a href="#find">Find</a></li>
				          <li><a href="#view">View Blockchain</a></li>
				          <li><a href="#blog">Blog</a></li>
				          <li class="menu-has-children"><a href="">Pages</a>
				            <ul>
				              <li><a href="content.html">Generic</a></li>
				              <li><a href="help.html">Elements</a></li>
				            </ul>
				          </li>
				        </ul>
				      </nav><!-- #nav-menu-container -->		    		
			    	</div>
			    </div>
			  </header><!-- #header -->

			<!-- start banner Area -->
			<section class="banner-area relative" id="home">
				<div class="overlay overlay-bg"></div>		
				<div class="container">
					<div class="row fullscreen d-flex align-items-center justify-content-start">
						<div id="peer" class="banner-content col-lg-12 col-md-12">
							
							<form action="/addPeer" method="POST">
								<input type="text" name="peer" placeholder="enter your ip" class="form-control mb-20">
								<input type="submit" value ="Add as Peer" class="primary-btn header-btn text-uppercase"></form>
								
						</div>												
					</div>
				</div>
			</section>
			<!-- End banner Area -->	

			<!-- Start convert Area -->
			<section class="convert-area" id="add">
				<div class="container">
					<div class="convert-wrap">
						<div class="row justify-content-center align-items-center flex-column pb-30">
							<h1 class="text-white">Add Your Blocks!!</h1>
							<p class="text-white">Who are in extremely love with eco friendly system.</p>							
						</div>
						<div class="row justify-content-center align-items-start">
							<div class="col-lg-2 cols-img">
								<img class="d-block mx-auto" src="img/blockdoc.png" style="width:110px;height:110px; alt="">
							</div>
							
							<div class="col-lg-3 cols">
								<form action="/" method="POST" name="myform">
								<input type="text" name="name" placeholder="enter your name" class="form-control mb-20">
								<input type="text" name="id" placeholder="enter document id" class="form-control mb-20">
								<input type="submit" class="primary-btn header-btn text-uppercase mb-20" value="submit"></form>
							</div>
						</div>						
					</div>
				</div>	
			</section>
			<!-- End convert Area -->
			

			<!-- Start simple-services Area -->
			<section class="simple-services-area section-gap">
				<div class="container">
					<div class="row">
						<div class="col-lg-4 single-services">
							<img src="img/secure.png" style="width:60px;height:60px"; alt="">
							<a href="#"><h4 class="pt-30 pb-20">Secure</h4></a>
							<p>
								Data is encrypted to the core. It is near impenetrable.Sleep Free
							</p>
						</div>
						<div class="col-lg-4 single-services">
							<img src="img/p2p.png" style="width:60px;height:60px"; alt="">
							<a href="#"><h4 class="pt-30 pb-20">Blockchain Exchang</h4></a>
							<p>
								Blockchain Blockbuster							</p>
						</div>
						<div class="col-lg-4 single-services">
							<img src="img/s3.png" alt="">
							<a href="#"><h4 class="pt-30 pb-20">Work with Blockchain</h4></a>
							<p>
								Blockchain Blockbuster							</p>
						</div>												
					</div>
				</div>	
			</section>
			<!-- End simple-services Area -->
			

			<!-- Start about Area -->
			<section class="aboutus-area">
				<div class="container-fluid">
					<div class="row d-flex align-items-center">
						<div class="col-lg-6 aboutus-left no-padding">
							<div class="active-about-carusel">
								<img class="img-fluid item" src="img/bbb.jpg" alt="">
								<img class="img-fluid item" src="img/bbb.jpg" alt="">
								<img class="img-fluid item" src="img/bbb.jpg" alt="">
								<img class="img-fluid item" src="img/bbb.jpg" alt="">
							</div>
						</div>
						<div class="col-lg-6 aboutus-right no-padding">
							<img src="img/ico.png" alt="">
							<h1 class="pt-40 pb-30">
								maintaining docs <br>
								is not that tough <br>
								Anymore
							</h1>
							<p>Handle your own data safely!!!!
								
							</p>
						</div>
					</div>
				</div>	
			</section>
			<!-- End about Area -->			

			<!-- Start service Area--> 
			<section class="service-area section-gap" id="find">
				<div class="container">
					<div class="row d-flex justify-content-center">
						<div class="col-md-9 pb-40 header-text">
							<h1>Find Your Block</h1>
							<p><form action="/findBlock" method="POST"> 
								Enter Id<input type="text" name="hash">
								<input type="submit" value="Find" class="primary-btn header-btn text-uppercase"></form>
							</p>
						</div>
					</div>
					<div class="row">
						<div class="col-lg-4 col-md-6">
							<div class="single-service">
								<h1 id="block"><span class="lnr lnr-user"></span></h1>
								<p id="name">
									
								</p>
							</div>
						</div>
						<div class="col-lg-4 col-md-6">
							<div class="single-service">
								<h4><span class="lnr lnr-license"></span>Professional Service</h4>
								<p>
									Usage of the Internet is becoming more common due to rapid advancement of technology and power.
								</p>								
							</div>
						</div>
						<div class="col-lg-4 col-md-6">
							<div class="single-service">
								<h4><span class="lnr lnr-phone"></span>Great Support</h4>
								<p>
									Usage of the Internet is becoming more common due to rapid advancement of technology and power.
								</p>								
							</div>
						</div>
						<div class="col-lg-4 col-md-6">
							<div class="single-service">
								<h4><span class="lnr lnr-rocket"></span>Technical Skills</h4>
								<p>
									Usage of the Internet is becoming more common due to rapid advancement of technology and power.
								</p>				
							</div>
						</div>
						<div class="col-lg-4 col-md-6">
							<div class="single-service">
								<h4><span class="lnr lnr-diamond"></span>Highly Recomended</h4>
								<p>
									Usage of the Internet is becoming more common due to rapid advancement of technology and power.
								</p>								
							</div>
						</div>
						<div class="col-lg-4 col-md-6">
							<div class="single-service">
								<h4><span class="lnr lnr-bubble"></span>Positive Reviews</h4>
								<p>
									Usage of the Internet is becoming more common due to rapid advancement of technology and power.
								</p>									
							</div>
						</div>						
					</div>
				</div>	
			</section> 
			End service Area -->		
						

			<!-- Start stat Area -->
			<section class="stat-area section-gap" id="view">
				<div class="container">
					<div class="row justify-content-center align-items-center">
						<div class="col-lg-6 stat-left">
							<table class="table table-inverse">
										<thead>
											<tr><th>Index</th>
												<th>Name</th>
												<th>Id</th>
												<th>TimeStamp</th>
												<th>Status</th>
											</tr>
										</thead>
										<tbody><tr><% for(var i=0 ;i < blockchain.length ; i++) {%>
												<td><%= blockchain[i].index%></td>
												<td><%= blockchain[i].name%></td>
												<td><%= blockchain[i].id%></td>
												<td><%= blockchain[i].timestamp%></td>
												<td><%= blockchain[i].status%></td>

											</tr>
											<%}%></tbody></table>
						</div>
					</div>

						</div>
						<div class="col-lg-6 stat-right">
							<h1>Real Time View <br>
							of Blockchain (Realtime)</h1>
							<p class="pt-20 pb-20">
								
							<form action="/blocks" method="GET">
							<input type="submit" value="view" class="primary-btn header-btn text-uppercase"></form></p>
						</div>
					</div>
				</div>	
			</section>
			<!-- End stat Area -->
			

			<!-- Start callaction Area -->
			<section class="callaction-area section-gap">
				<div class="container">
					<div class="row justify-content-center">
						<div class="col-lg-9">
							<h1 class="text-white">Blockchain-currently trending</h1>
							<p class="text-white">
								Cab mobility is a great candidate for blockchain technology. One issue in kick-starting this is agreeing on a software solution from several blockchains/smart-contracts products or services.
							</p>
							<a href="#" class="primary-btn">Makes u feel good !!!!</a>							
						</div>
					</div>
				</div>	
			</section>
			<!-- End callaction Area -->
			

			<!-- Start price Area 
			<section class="price-area pt-100" id="price">
				<div class="container">
					<div class="row d-flex justify-content-center">
						<div class="menu-content pb-60 col-lg-8">
							<div class="title text-center">
								<h1 class="mb-10">Purchase whatever you want</h1>
								<p>Who are in extremely love with eco friendly system.</p>
							</div>
						</div>
					</div>						
					<div class="row">
						<div class="col-lg-4">
							<div class="single-price no-padding">
								<div class="price-top">
									<h4>01 Ripple</h4>
								</div>
								<p>
									Who are in extremely love with <br>
									eco friendly system.
								</p>
								<div class="price-bottom">
									<h1><span>$</span> 7999</h1>
									<a href="#" class="primary-btn header-btn">Get Started</a>
								</div>
							</div>
						</div>
						<div class="col-lg-4">
							<div class="single-price no-padding">
								<div class="price-top">
									<h4>01 Ethereum</h4>
								</div>
								<p>
									Who are in extremely love with <br>
									eco friendly system.
								</p>
								<div class="price-bottom">
									<h1><span>$</span> 9999</h1>
									<a href="#" class="primary-btn header-btn">Get Started</a>
								</div>
							</div>
						</div>
						<div class="col-lg-4">
							<div class="single-price no-padding">
								<div class="price-top">
									<h4>01 Bitcoin</h4>
								</div>
								<p>
									Who are in extremely love with <br>
									eco friendly system.
								</p>
								<div class="price-bottom">
									<h1><span>$</span> 5999</h1>
									<a href="#" class="primary-btn">Get Started</a>
								</div>
							</div>				
						</div>								
					</div>
				</div>	
			</section>
			<!-- End price Area -->
		

			<!-- Start blog Area -
				<section class="blog-area section-gap" id="blog">
					<div class="container">
						<div class="row d-flex justify-content-center">
							<div class="menu-content pb-60 col-lg-8">
								<div class="title text-center">
									<h1 class="mb-10">Latest Posts from our Blog</h1>
									<p>Who are in extremely love with eco friendly system.</p>
								</div>
							</div>
						</div>						
						<div class="row">
							<div class="col-lg-4 single-blog">
								<div class="thumb">
									<img class="img-fluid" src="img/b1.jpg" alt="">
								</div>
								<div class="desc">
									<a href="#"><h4>Portable Fashion for women</h4></a>
									<p>
										Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
									</p>
									<div class="user d-flex flex-row">
										<div>
											<img class="img-fluid" src="img/b4.jpg" alt="">
										</div>
										<div class="meta">
											<h6>Belle Beck</h6>
											<p>January 18th, 2018 at 17.21 </p>
										</div>
									</div>
								</div>
							</div>
							<div class="col-lg-4 single-blog">
								<div class="thumb">
									<img class="img-fluid" src="img/b2.jpg" alt="">
								</div>
								<div class="desc">
									<a href="#"><h4>Portable Fashion for women</h4></a>
									<p>
										Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna al.
									</p>
									<div class="user d-flex flex-row">
										<div>
											<img class="img-fluidrc="img/b5.jpg" alt="">
										</div>
										<div class="meta">
											<h6>Harriet Barrett</h6>
											<p>January 18th, 2018 at 17.21 </p>
										</div>
									</div>
								</div>
							</div>
							<div class="col-lg-4 single-blog">
								<div class="thumb">
									<img class="img-fluid" src="img/b3.jpg" alt="">
								</div>
								<div class="desc">
									<a href="#"><h4>Portable Fashion for women</h4></a>
									<p>
										Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
									</p>
									<div class="user d-flex flex-row">
										<div>
											<img class="img-fluid" src="img/b6.jpg" alt="">
										</div>
										<div class="meta">
											<h6>Fannie Simmons</h6>
											<p>January 18th, 2018 at 17.21 </p>
										</div>
									</div>
								</div>
							</div>														
						</div>
					</div>	
				</section>
				 End blog Area -->
					

			<!-- start footer Area 		
			<footer class="footer-area section-gap">
				<div class="container">
					<div class="row">
						<div class="col-lg-3  col-md-6 col-sm-6">
							<div class="single-footer-widget">
								<h4 class="text-white">About Us</h4>
								<p>
									okok.
								</p>
							</div>
						</div>
						<div class="col-lg-3  col-md-6 col-sm-6">
							<div class="single-footer-widget">
								<h4 class="text-white">Top Products</h4>
								<ul class="footer-menu">
									<li><a href="#">Managed Website</a></li>
									<li><a href="#">Managed Reputation</a></li>
									<li><a href="#">Managed Tools</a></li>
									<li><a href="#">Managed Service</a></li>
								</ul>
									
							</div>
						</div>						
						<div class="col-lg-6  col-md-6 col-sm-6">
							<div class="single-footer-widget">
								<h4 class="text-white">Newsletter</h4>
								<p>You can trust us. we only send  offers, not a single spam.</p>
								<div class="d-flex flex-row" id="mc_embed_signup">
									  <form class="navbar-form" novalidate="true" action="https://spondonit.us12.list-manage.com/subscribe/post?u=1462626880ade1ac87bd9c93a&amp;id=92a4423d01" method="get">
									    <div class="input-group add-on">
									      	<input class="form-control" name="EMAIL" placeholder="Email address" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Email address'" required="" type="email">
											<div style="position: absolute; left: -5000px;">
												<input name="b_36c4fd991d266f23781ded980_aefe40901a" tabindex="-1" value="" type="text">
											</div>
									      <div class="input-group-btn">
									        <button class="genric-btn"><span class="lnr lnr-arrow-right"></span></button>
									      </div>
									    </div>
									      <div class="info mt-20"></div>									    
									  </form>
								</div>
							</div>
						</div>						
					</div>
					<!--<div class="footer-bottom d-flex justify-content-between align-items-center flex-wrap">
						<p class="footer-text m-0">
						
						</p>
						<div class="footer-social d-flex align-items-center">
							<a href="#"><i class="fa fa-facebook"></i></a>
							<a href="#"><i class="fa fa-twitter"></i></a>
							<a href="#"><i class="fa fa-dribbble"></i></a>
							<a href="#"><i class="fa fa-behance"></i></a>
						</div>
					</div>
				</div>
			</footer>	
			<!-- End footer Area -->

			<script src="js/vendor/jquery-2.2.4.min.js"></script>
			<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
			<script src="js/vendor/bootstrap.min.js"></script>			
			<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBhOdIF3Y9382fqJYt5I_sswSrEw5eihAA"></script>
  			<script src="js/easing.min.js"></script>			
			<script src="js/hoverIntent.js"></script>
			<script src="js/superfish.min.js"></script>	
			<script src="js/jquery.ajaxchimp.min.js"></script>
			<script src="js/jquery.magnific-popup.min.js"></script>	
			<script src="js/owl.carousel.min.js"></script>			
			<script src="js/jquery.sticky.js"></script>
			<script src="js/jquery.nice-select.min.js"></script>			
			<script src="js/parallax.min.js"></script>	
			<script src="js/waypoints.min.js"></script>
			<script src="js/jquery.counterup.min.js"></script>			
			<script src="js/mail-script.js"></script>	
			<script src="js/main.js"></script>	
		</body>
	</html>




    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

# Part 2 - Mining our Blockchain

# Creating a Web App
app = Flask(__name__)

# Creating a Blockchain
blockchain = Blockchain()

# Mining a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200

# Getting the full Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The Blockchain is valid.'}
    else:
        response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return jsonify(response), 200

# Running the app
app.run(host = '0.0.0.0', port = 5000)
