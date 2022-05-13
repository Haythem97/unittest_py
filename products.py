from flask import Flask, make_response,request,jsonify
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_HOST"] = "mongodb+srv://haythem:haythem@cluster0.q4qnp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
db = MongoEngine()
db.init_app(app)


class Product(db.Document):
    prod_id = db.IntField()
    Title = db.StringField()
    Color = db.StringField()
    Price = db.StringField()


    def to_json(self):
        #convert le document en JSON
        return {
            "prod_id": self.prod_id,
            "Title": self.Title,
            "Color": self.Color,
            "Price": self.Price
        }
    
@app.route('/api/create_product',methods=['POST'])
def create_product():
    prod = Product(prod_id= 15, Title= "Nike Air Force 1",Color= "White", Price="120")
    prod.save()
    return make_response("",201)

@app.route('/api/products',methods=['GET','POST'])
def api_products():
    if request.method == "GET": 
        products = []
        for product in Product.objects:
            products.append(product)
        return make_response(jsonify(products),200)
    elif request.method == "POST": 
        content = request.json
        product = Product(prod_id=content['prod_id'],
        Title=content['Title'],
        Color=content['Color'],
        Price=content['Price'])
        product.save()
        return make_response("Produit enregistré",201)

    

@app.route('/api/products/<prod_id>',methods=['GET','PUT','DELETE'])
def api_each_prod(prod_id):
    
    if request.method == "GET":
        product_obj = Product.objects(prod_id=prod_id).first()
        return make_response(jsonify(product_obj.to_json()),200)
    

        
    elif request.method == "PUT":
        product_obj = Product.objects(prod_id=prod_id).first()
        product_obj.update(prod_id=1,Title="Adidas",Color="Black",Price="156")
        return make_response("Produit modifier",200)


    elif request.method == "DELETE":
        product_obj = Product.objects(prod_id=prod_id).first()
        product_obj.delete()
        return make_response("Produit supprimé",200)
     
if __name__ == '__main__':
    app.run()
    
