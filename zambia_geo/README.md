# Zambia Geo

A Python package containing Zambian provinces and cities data.

## Features

* List all Zambian provinces
* Get cities for each province
* Search for cities
* Validate province and city names

## How to Use Locally

1. Create a virtual environment:
```bash```
    
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Install the package in development mode:

    pip install -e .

3. Run Tests

    python -m pytest tests/

### Now you can import and use the package in your Python code:

    from zambia_geo import get_all_provinces, get_province_cities
    # Get all provinces
    provinces = get_all_provinces()
    for province in provinces:
        print(province.name, province.capital)

    # Get cities in a province
    cities = get_province_cities("Lusaka")
    for city in cities:
        print(city.name, city.population)

## Usage in Django

To use zambia_geo package in Django model choice fields, you'll need to create choices tuples from the package's data. Here's how you can implement this:

### Example Django Model Usage

    from django.db import models
    from zambia_geo.utils import get_province_choices, get_city_choices

    class UserProfile(models.Model):
        # Province field
        province = models.CharField(
            max_length=50,
            choices=get_province_choices(),
            blank=True,
            null=True
        )
        
        # City field that depends on province
        city = models.CharField(
            max_length=50,
            choices=[],
            blank=True,
            null=True
        )
        
        class Meta:
            verbose_name = "User Profile"
            verbose_name_plural = "User Profiles"
        
        def __str__(self):
            return f"{self.province} - {self.city}"

## Dynamic City Choices Based on Province (Forms)

To make the city choices dynamic based on the selected province, you'll need to use JavaScript or Django's form facilities:

**Option 1: Using Django Forms with JavaScript:**

    # forms.py
    from django import forms
    from .models import UserProfile
    from zambia_geo.utils import get_province_choices

    class UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ['province', 'city']
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['province'].choices = get_province_choices()
            self.fields['city'].choices = []
            
            if 'province' in self.data:
                try:
                    province_name = self.data.get('province')
                    self.fields['city'].choices = get_city_choices(province_name)
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk and self.instance.province:
                self.fields['city'].choices = get_city_choices(self.instance.province)

**Option 2: JavaScript Implementation:**

If you prefer a pure JavaScript solution, here's how to implement it:

    <!-- In your template -->
    <form method="post">
        {% csrf_token %}
        
        <div class="form-group">
            <label for="province">Province</label>
            <select class="form-control" id="province" name="province">
                <option value="">Select Province</option>
                {% for value, label in province_choices %}
                    <option value="{{ value }}" {% if value == selected_province %}selected{% endif %}>{{ label }}</option>
                {% endfor %}
            </select>
        </div>
        
        <div class="form-group">
            <label for="city">City</label>
            <select class="form-control" id="city" name="city">
                <option value="">Select City</option>
                {% for value, label in city_choices %}
                    <option value="{{ value }}" {% if value == selected_city %}selected{% endif %}>{{ label }}</option>
                {% endfor %}
            </select>
        </div>
        
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>

    <script>
    document.getElementById('province').addEventListener('change', function() {
        const province = this.value;
        const citySelect = document.getElementById('city');
        
        // Clear existing options
        citySelect.innerHTML = '<option value="">Select City</option>';
        
        if (province) {
            // Fetch cities for the selected province
            fetch(`/api/cities/?province=${province}`)
                .then(response => response.json())
                .then(data => {
                    data.cities.forEach(city => {
                        const option = document.createElement('option');
                        option.value = city.name;
                        option.textContent = city.name;
                        citySelect.appendChild(option);
                    });
                });
        }
    });
    </script>

### Create an API endpoint for cities (optional)

    # views.py
    from django.http import JsonResponse
    from zambia_geo import get_province_cities

    def get_cities(request):
        province = request.GET.get('province')
        if province:
            cities = get_province_cities(province)
            cities_data = [{'name': city.name} for city in cities]
            return JsonResponse({'cities': cities_data})
        return JsonResponse({'cities': []})

    # urls.py
    from django.urls import path
    from .views import get_cities

    urlpatterns = [
        path('api/cities/', get_cities, name='get_cities'),
        # other URLs...
    ]

### Admin Integration
To use these choices in Django admin:

    # admin.py
    from django.contrib import admin
    from .models import UserProfile
    from zambia_geo.utils import get_province_choices, get_city_choices

    class UserProfileAdmin(admin.ModelAdmin):
        list_display = ('province', 'city')
        
        def get_form(self, request, obj=None, **kwargs):
            form = super().get_form(request, obj, **kwargs)
            form.base_fields['province'].choices = get_province_choices()
            
            if obj and obj.province:
                form.base_fields['city'].choices = get_city_choices(obj.province)
            else:
                form.base_fields['city'].choices = []
            
            return form

    admin.site.register(UserProfile, UserProfileAdmin)