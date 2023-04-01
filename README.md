# ABAC: A Design of Attribute-based Access Control Model for Microservice Security Manager Using API Gateway
## Abstract
This project proposes a design of an attribute-based access control (ABAC) model for microservice security management using an API gateway. Microservices have become a popular architectural style for developing complex applications, but managing security in a microservice environment is challenging. ABAC is a flexible and dynamic access control model that can provide fine-grained access control based on user attributes. In this project, we present a design of an ABAC model that integrates with an API gateway to manage access control for microservices. The proposed model uses a policy engine to evaluate access requests based on the user attributes and service attributes. A set of attributes that are used to make access control decisions. These attributes may be gathered from various sources, including user profiles, device information, and other metadata. We also present a case study that demonstrates the effectiveness of our proposed model in managing access control for microservices. The results show that our model can provide fine-grained access control and improve the overall security of microservice environments.

## Scenario 
A Financial Company is a large financial institution that deals with a vast amount of sensitive financial information on a daily basis. They have recently identified the need to improve their access control system to ensure the confidentiality, integrity, and availability of their data. One day, a new employee is hired to work in your department, but they are not properly vetted or their background check is incomplete.

As a result, this employee has access to all of the company's data, including sensitive information that should only be accessible to a select few. They may not have malicious intent, but they may accidentally leak sensitive information, share it with unauthorized individuals, or even steal it for personal gain.

Without proper access management, this situation could have disastrous consequences for the company, including reputation damage, legal liabilities, and financial losses. The company may also face regulatory penalties for failing to adequately protect its data.

### Assets need to be protected
- Company sensitive data
- Custommer infomation
### Related-Party 
- Admin
- Advisor
- Employees
- Customer
- Adversaries
### Security goal
- Access only by authorized parties
- Lowest authority

## Solution

RBAC or ABAC?

RBAC still a widely used access control model in many organizations. However, there are some limitations to RBAC  that may make it less suitable for this scenarios. RBAC policies are typically based on a user's role and do not consider other factors, such as the user's location, time of day, or the sensitivity of the data being accessed. This can result in overprivileged access, where users are given more access rights than they need to perform their job functions, creating potential security risks. They have decided to implement ABAC to achieve this goal.

<p align="center">
<img src="https://user-images.githubusercontent.com/88936785/227706076-dddc61bc-0c42-45f5-b0e2-5a20f8a6f266.png">
<p align="center">Figure 1. ABAC and API gateway model</p>
</p>

A financial institution has an API gateway that exposes customer account information to authorized users. The financial institution may have different types of users with different levels of access to customer account information, such as customer service representatives, financial advisors, and executives.

The financial institution could use ABAC to define access control policies based on user attributes such as job role, department, and location. For example, the financial institution could define an access control policy that allows customer service representatives to view basic customer account information, such as account balance and transaction history. The policy could also include restrictions on which customer accounts each representative can access based on the representative's department or location.

On the other hand, the financial institution could define an access control policy that allows financial advisors to view more detailed customer account information, such as investment portfolio performance and risk assessments. The policy could also restrict access to sensitive financial data, such as customer credit scores or financial statements, to only authorized users with the appropriate clearance level.

Finally, the financial institution could define an access control policy that allows executives to view high-level financial reports and analytics, such as revenue forecasts and budget projections. The policy could also include restrictions on which financial reports each executive can access based on their job role or department. 

By using ABAC to define access control policies based on user attributes, the financial institution can ensure that only authorized users with the appropriate permissions and clearances can access customer account information, reducing the risk of unauthorized access and data breaches.

## Resources
|Resources| |
| :------------ |:---------------|
| Cloud | Deploy server, database storage |
| Database |  MySQL |
| Libraries | Flask, Flask-abac | 
| Hardware | Intel core I5, RAM 16GB |
| Programing languages | Python, HTML, CSS, Javascript |
## Contributor

| Full name  | ID  | Github | Job assignment | 
| :------------ |:---------------:| :-----------------------------------: | :----------------------- |
| Le Phu Duc    | 21521962        | [Jinn](https://github.com/lephuduc)   |  |
| Le Xuan Hoang | 21522090        | [Enkai](https://github.com/LaiLaK918) |  |
| Tran Cong Thanh  | 21521450     | [PkNova](https://github.com/PkNova76) |  |
