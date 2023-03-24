# ABAC A Design of Attribute-based Access Control Model for Microservice Security Manager Using API Gateway
## Abstract
This paper proposes a design of an attribute-based access control (ABAC) model for microservice security management using an API gateway. Microservices have become a popular architectural style for developing complex applications, but managing security in a microservice environment is challenging. ABAC is a flexible and dynamic access control model that can provide fine-grained access control based on user attributes. In this paper, we present a design of an ABAC model that integrates with an API gateway to manage access control for microservices. The proposed model uses a policy engine to evaluate access requests based on the user attributes and service attributes. The policy engine uses a rule-based approach to match access requests with policies and make authorization decisions. We also present a case study that demonstrates the effectiveness of our proposed model in managing access control for microservices. The results show that our model can provide fine-grained access control and improve the overall security of microservice environments.
## Scenario 
A financial institution has an API gateway that exposes customer account information to authorized users. The financial institution may have different types of users with different levels of access to customer account information, such as customer service representatives, financial advisors, and executives.

The financial institution could use ABAC to define access control policies based on user attributes such as job role, department, and location. For example, the financial institution could define an access control policy that allows customer service representatives to view basic customer account information, such as account balance and transaction history. The policy could also include restrictions on which customer accounts each representative can access based on the representative's department or location.

On the other hand, the financial institution could define an access control policy that allows financial advisors to view more detailed customer account information, such as investment portfolio performance and risk assessments. The policy could also restrict access to sensitive financial data, such as customer credit scores or financial statements, to only authorized users with the appropriate clearance level.

Finally, the financial institution could define an access control policy that allows executives to view high-level financial reports and analytics, such as revenue forecasts and budget projections. The policy could also include restrictions on which financial reports each executive can access based on their job role or department. 

By using ABAC to define access control policies based on user attributes, the financial institution can ensure that only authorized users with the appropriate permissions and clearances can access customer account information, reducing the risk of unauthorized access and data breaches.

## Contributor

| Full name  | ID  | Github |
| :------------ |:---------------:| :-----:|
| Le Phu Duc    | 21521962        | [Jinn](https://github.com/lephuduc) |
| Le Xuan Hoang | 21522019        |  [Enkai](https://github.com/LaiLaK918)  |
| Tran Cong Thanh  | 21521450     |    [PkNova](https://github.com/PkNova76) |
