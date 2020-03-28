def format_bytes(size):
    
    power = 2**10
    n=0
    power_labels = {0:'Kilobytes', 1:'Megabytes', 2:'Gigabytes', 3:'Terabytes'}
    while size > power:
        size /=power
        n +=1
    return round(size,1), power_labels[n]



print(format_bytes(75654))