# Generated by Django 5.0.7 on 2024-07-19 00:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('BlockID', models.AutoField(primary_key=True, serialize=False)),
                ('BlockName', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
                ('Address', models.TextField()),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('Position', models.CharField(max_length=50)),
                ('DateHired', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('ShiftID', models.AutoField(primary_key=True, serialize=False)),
                ('ShiftName', models.CharField(max_length=50)),
                ('StartTime', models.TimeField()),
                ('EndTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('AttendanceID', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateField()),
                ('CheckInTime', models.TimeField()),
                ('CheckOutTime', models.TimeField()),
                ('EmployeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Security.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('LeaveID', models.AutoField(primary_key=True, serialize=False)),
                ('LeaveType', models.CharField(max_length=20)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Reason', models.TextField()),
                ('Status', models.CharField(max_length=20)),
                ('EmployeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Security.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('AssignmentID', models.AutoField(primary_key=True, serialize=False)),
                ('DayOfWeek', models.CharField(max_length=10)),
                ('BlockID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Security.block')),
                ('EmployeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Security.employee')),
                ('ShiftID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Security.shift')),
            ],
        ),
    ]