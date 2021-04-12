- hosts: web
  vars_files:
      - "{{ ansible_facts['os_family'] }}.yml"
  tasks:
  - name: "TASK 10"
    block:
       - name: "installing httpd"    
         package:
            name: "{{ Soft }}"
            state: present    
       - name: "content writing in webpage"
         copy:
             dest: /var/www/html/task.html
             content: "{{ content }}"
       - name: "starting the service"
         service:
              name: "{{ Soft }}"
              state: started
    always:
      - debug:
          msg: "THANK YOU"

