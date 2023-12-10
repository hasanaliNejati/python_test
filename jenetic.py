import random

# فرمول مورد نظر (ax)
def equation(a, x):
    return a * x

# مقدار هدف یا تابع فیتنس (فاصله داده‌های واقعی و محاسبه شده)
def fitness_function(a, data):
    total_error = 0
    for x, y in data:
        predicted = equation(a, x)
        total_error += abs(predicted - y)
    return total_error

# تولید جمعیت اولیه
def initial_population(pop_size):
    return [random.uniform(-10, 10) for _ in range(pop_size)]  # محدوده مقادیر a

# انتخاب اعضا بر اساس تابع فیتنس
def selection(population, data):
    return min(population, key=lambda a: fitness_function(a, data))

# تلاقی اعضا
def crossover(parent1, parent2):
    return (parent1 + parent2) / 2.0

# جهش
def mutation(child):
    mutation_rate = 0.1
    if random.random() < mutation_rate:
        return child + random.uniform(-1, 1)
    return child

# الگوریتم ژنتیک
def genetic_algorithm(population_size, generations, data):
    population = initial_population(population_size)
    
    for _ in range(generations):
        parents = random.sample(population, 2)
        child = crossover(parents[0], parents[1])
        child = mutation(child)
        
        population.remove(max(population, key=lambda a: fitness_function(a, data)))
        population.append(child)
    
    best_solution = selection(population, data)
    return best_solution

# داده‌های ورودی به صورت (x, y)
data = [(1, 5), (2, 10), (3, 15)]  # مثالی از داده‌های واقعی

population_size = 20
generations = 100

best_a = genetic_algorithm(population_size, generations, data)
print("بهینه‌ترین مقدار a:", best_a)
