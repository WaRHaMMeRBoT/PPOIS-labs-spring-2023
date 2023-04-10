import Train

class Railway_station:
    def __init__(self,rs_number):
        self.stock=[]
        self.set_rs_number(rs_number)   
    
    def set_rs_number(self,number):
        self.rs_number=number
    
    def get_rs_number(self):
        return self.rs_number
    
    def load_to_stock(self,cargo_type,cargo_quantity):
        if self.stock:
            for item in self.stock:
                if cargo_type in item:
                    item[cargo_type] +=cargo_quantity
                    return
            else:
                self.stock.append({cargo_type:cargo_quantity})
        else:
                self.stock.append({cargo_type:cargo_quantity})

    def get_stock_info(self,cargo_type):
        for cargo in self.stock:
            if cargo_type in cargo:
                return True
        return False
    
    def get_all_stock_cargo(self):
        all_keys = set()
        for d in self.stock:
            all_keys.update(d.keys())
        return all_keys

    def unload_from_stock(self,cargo_type,cargo_quantity):
        res = [d for d in self.stock if d.get(cargo_type)]
        if res:
            self.stock.remove(res[0])
        else:
            print(f"{cargo_type} doesn't exist")
            return
        if res[0][cargo_type]-cargo_quantity < 0:
            print("exception too large value")
            return
        else:
            res[0][cargo_type]-=cargo_quantity
        if res[0][cargo_type]==0:
            return
        else:
            self.stock.append(res[0])
        
    def load_train(self,train:Train,cargo_type,cargo_quantity):
        self.unload_from_stock(cargo_type,cargo_quantity)
        load_per_traincar=round((cargo_quantity/len(train.get_trainCars())))
        for traincar in train.get_trainCars():
            traincar.load(cargo_type,load_per_traincar)
    
    def unload_train(self,train:Train):
        type=train.get_trainCars()[0].get_cargo_type()
        for train in train.get_trainCars():
            self.load_to_stock(type,train.unload(type))
        
    def __str__(self):
        return f"RSNumber: {self.rs_number}\n{self.stock}"
