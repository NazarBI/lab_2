def calculate_estimate(a, m, b):
    E = (a + 4*m + b) / 6
    SD = (b - a) / 6
    return E, SD

def calculate_confidence_interval(estimate, standard_deviation):
    lower_bound = estimate - 2 * standard_deviation
    upper_bound = estimate + 2 * standard_deviation
    return lower_bound, upper_bound

def main():
    # Запитуємо користувача про вхідні оцінки для завдання
    a = float(input("Введіть оцінку 'a' для завдання: "))
    m = float(input("Введіть оцінку 'm' для завдання: "))
    b = float(input("Введіть оцінку 'b' для завдання: "))

    # Розраховуємо оцінку і стандартне відхилення для завдання
    task_estimate, task_standard_deviation = calculate_estimate(a, m, b)

    # Розраховуємо оцінку та стандартне відхилення для проекту
    project_estimate = task_estimate
    project_standard_deviation = task_standard_deviation

    # Розраховуємо довірчий інтервал для проекту
    lower_bound, upper_bound = calculate_confidence_interval(project_estimate, project_standard_deviation)

    # Виводимо результати
    print(f"Project's 95% confidence interval: {lower_bound} ... {upper_bound} points")

if __name__ == "__main__":
    main()
