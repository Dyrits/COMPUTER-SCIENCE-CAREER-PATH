from datetime import datetime, timedelta

class Art():
    def __init__(self, artist, title, medium, year, owner = None):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self):
        if self.owner:
            return f"{self.artist}. {self.title}, {self.year}, {self.medium}. Owned by {self.owner.name}, {self.owner.location}."
        else:
            return f"{self.artist}. {self.title}, {self.year}, {self.medium}."
    

girl_with_mandolin = Art(
    "Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil in canvas", 1910)

# print(girl_with_mandolin)

class Marketplace():
    def __init__(self, listings = []):
        self.listings = listings
        
    def add_listing(self, new_listing):
        self.listings.append(new_listing)
        
    def remove_listing(self, listing):
        self.listings.remove(listing)
         
    def show_listings(self):
        [print(listing) for listing in self.listings]
        if not self.listings:
            print("We have nothing to sell for the moment.")
        
    def check_expiration(self):
        for listing in self.listings:
            if listing.expiration_date > datetime.now:
                self.remove_listing(listing)
        
veneer = Marketplace()

# veneer.show_listings()

class Client():
    def __init__(self, name, wallet, is_museum, location=None):
        self.name = name
        self.location = "Private Collection" if not is_museum else location
        self.is_museum = is_museum
        self.wallet = wallet
    
    def __repr__(self):
        return f"{self.name}, {self.location}. Capital: ${self.wallet}M"
        
    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)
            
    def buy_artwork(self, artwork):
        if artwork.owner != self:
            for listing in veneer.listings:
                if artwork == listing.art:
                    if self.wallet > listing.price:
                        artwork.owner.wallet += listing.price
                        self.wallet -= listing.price
                        artwork.owner = self
                        veneer.remove_listing(listing)
                        break
                
        
edytta = Client("Edytta Halpirt", 0, False)
moma = Client("The MOMA", 10, True, "New York")
girl_with_mandolin.owner = edytta
# print(girl_with_mandolin)

class Listing():
    def __init__(self, art, price, seller, expiration_date = datetime.now() + timedelta(30)):
        self.art = art
        self.price = price
        self.seller = seller
        self.expiration_date = expiration_date
        
    def __repr__(self):
        return f"{self.art.title} | Price: ${self.price} | Available until: {self.expiration_date.strftime('%Y/%m/%d')}"

# TESTS
edytta.sell_artwork(girl_with_mandolin, 6)
print(girl_with_mandolin)
print(edytta)
print(moma)
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print()
print(girl_with_mandolin)
print(edytta)
print(moma)
veneer.show_listings()

