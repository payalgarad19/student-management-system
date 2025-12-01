# Student Management System

A Python-based command-line application for managing student records at TheKiranAcademy. This system handles student enrollment, fee management, and data filtering.

## Features

### 1. Add Student Details
- Register new students with auto-generated registration numbers
- Select from available courses (Python, Java, AWS)
- Apply discount percentages on course fees
- Accept partial fee payments
- Automatic calculation of remaining fees
- Records admission date automatically

### 2. Display Student Details
- View all student records in a formatted table
- Shows: Registration number, Name, City, Course, Total fee, Paid fee, Remaining fee, and Admission date

### 3. Update Student Details
- **Change Course**: Update student's enrolled course
- **Fee Payment**: Accept additional fee payments and update remaining balance automatically

### 4. Delete Student Details
- Remove student records by registration number

### 5. Filter Records
- **By Course**: Display all students enrolled in a specific course
- **By City**: (Feature placeholder - ready for implementation)

### 6. Exit
- Close the application

## Course Offerings

| Course | Fee (₹) |
|--------|---------|
| Python | 4,000 |
| Java   | 5,000 |
| AWS    | 3,000 |

## Installation

### Prerequisites
- Python 3.x installed on your system

### Setup
1. Clone or download the project files
2. No additional dependencies required (uses only Python standard library)

## Usage

### Running the Application
```bash
python student_management.py
```

### Sample Workflow

1. **Adding a Student**
   ```
   Select option: 1
   Enter student name: Rahul Sharma
   Enter city name: Mumbai
   Enter course name: python
   Enter discount in %: 10
   Your fee: 3600
   Enter fee amount: 1500
   ```

2. **Viewing All Students**
   ```
   Select option: 2
   ```
   Displays formatted table with all student records

3. **Updating Fee Payment**
   ```
   Select option: 3
   Enter reg: 101
   Select option: 2
   Enter amount: 1000
   ```

4. **Filtering by Course**
   ```
   Select option: 5
   Select option: 1
   Course: python
   ```

## Data Structure

The system uses a dictionary-based storage:

```python
{
    registration_number: {
        'name': 'Student Name',
        'city': 'City Name',
        'course': 'Course Name',
        't_fee': Total_Fee,
        'p_fee': Paid_Fee,
        'r_fee': Remaining_Fee,
        'add_date': 'DD/MM/YYYY'
    }
}
```

## Technical Details

- **Registration Numbers**: Auto-increment starting from 101
- **Date Format**: Automatically captures current date in ISO format (YYYY-MM-DD)
- **Fee Calculation**: Supports discount percentage with automatic total, paid, and remaining fee calculations
- **Data Persistence**: Currently stores data in memory (data lost on exit)

## Future Enhancements

- [ ] Implement city-based filtering
- [ ] Add data persistence (file/database storage)
- [ ] Generate fee receipts
- [ ] Add student search functionality
- [ ] Export reports to CSV/PDF
- [ ] Input validation and error handling improvements
- [ ] Add payment history tracking

## Sample Data

The system comes pre-loaded with one sample record:
- **Reg No**: 101
- **Name**: Payal Garad
- **City**: Pune
- **Course**: Python
- **Total Fee**: ₹4,000
- **Paid Fee**: ₹2,000
- **Remaining Fee**: ₹2,000

## Notes

- All fee amounts are in Indian Rupees (₹)
- Discount is applied as a percentage of the original course fee
- Registration numbers are automatically assigned sequentially
- Data is stored in memory and will be lost when the program exits

## Author

TheKiranAcademy

## License

This project is for educational purposes.
