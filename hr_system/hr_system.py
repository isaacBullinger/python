paycheck=float()

with open("hr_system/hr_system.txt") as employees:

    for line in employees:
        data=line.strip()
        data=data.split(' ')
        # print(data)
        name=data[0]
        id_number=data[1]
        job_title=data[2]
        salary=float(data[3])
        paycheck=(salary/12)/2
        # print(name)
        # print(f'Name: {name}, Title: {job_title}')
        # print(f'{name} (ID: {id_number}), {job_title} - ${salary:.2f}')
        # print(f'{name} ({id_number}), {job_title} - ${paycheck:.2f}')
        if job_title=='Engineer':
            paycheck=paycheck+1000
        print(f'{name} ({id_number}), {job_title} - ${paycheck:.2f}')