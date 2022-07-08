from django.db import models

class Item(models.Model):
	sname = models.CharField(max_length=40)
	fname = models.CharField(max_length=50)
	mname = models.CharField(max_length=50)
	age = models.CharField(max_length=40)
	add = models.CharField(max_length=100)
	contact = models.CharField(max_length=100)
	disease = models.CharField(max_length=100)
	specifydisease = models.CharField(max_length=100)
	plan = models.CharField(max_length=100)
	total = models.CharField(max_length=100)

	def __str__(self):
         return '%s-%s' % (self.sname, self.fname)

class ExercisePlan(models.Model):
	intensity = models.CharField(max_length=100)
	focus = models.CharField(max_length=100)
	

	#customerID = models.ForeignKey(Item, on_delete=models.CASCADE)
	
	
	def __str__(self):
		return self.intensity

class Program(models.Model):
	DietPlan = models.CharField(max_length=100)
	Trainer = models.CharField(max_length=100)
	Duration = models.CharField(max_length=100)

	#customerID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#planID = models.ForeignKey(Item, on_delete=models.CASCADE)

	
	def __str__(self):
		return self.DietPlan
	
class Products(models.Model):
	protein = models.CharField(max_length=100)
	gymbags = models.CharField(max_length=100)
	mat = models.CharField(max_length=100)
	others = models.CharField(max_length=100)
	Loss = models.CharField(max_length=100)
	locker = models.CharField(max_length=100)
	#customerID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#planID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#programID = models.ForeignKey(Item, on_delete=models.CASCADE)

	
	def __str__(self):
		return self.protein
	
class Feedback(models.Model):
	review = models.CharField(max_length=100)
	concern = models.CharField(max_length=100)
	complaints = models.CharField(max_length=100)
	

	#customerID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#planID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#programID = models.ForeignKey(Item, on_delete=models.CASCADE)
	#productID = models.ForeignKey(Item, on_delete=models.CASCADE)

	
	def __str__(self):
		return self.reviewID
	
