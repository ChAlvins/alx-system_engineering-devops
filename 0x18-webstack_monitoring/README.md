
# 0x18. Webstack monitoring


## Concepts

_For this project, we expect you to look at these concepts:_

-   [Monitoring]()
Just as the heart monitor in a hospital that is making sure that a patient’s heart is beating and at the right beat, software monitoring will watch computer metrics, record them, and emit an alert if something is unusual or that could make the computer not work properly happens.

`You cannot fix or improve what you cannot measure`  is a famous saying in the tech industry. In the age of the data-ism, monitoring how our software systems are doing is an important thing.

Web stack monitoring can be broken down into 2 categories:

-   Application monitoring: getting data about your running software and making sure it is behaving as expected
-   Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

### Here are few famous monitoring tools:

#### NewRelic

NewRelic requires you to add a piece of JavaScript to your website, this agent will collect information and send it back to the New Relic servers. It will give you a detailed analysis of how quickly your website loads in a browser, with a detailed analysis at every level of the stack. If the website is loading too slowly or users are experiencing error (500), there is a feature that allows you to trigger an alert. NewRelic now does much more than this, I’ll let you discover the rest.

#### DataDog

DataDog allows you to measure and monitor everything with graphs. It gathers performance data from all your application components. The service has a lot of integrations. You usually just need to properly configure your alert and you are good to go with solid monitoring coverage.

#### Uptime Robot

Uptime Robot is a simple service that will check that your website is responding from multiple locations in the world. This is the bare minimum when you host a website.

#### Nagios

Nagios is an open source project started in 1999, it is among the most widely used monitoring tools in the tech industry. It is, however, seen as outdated. Nagios had trouble adapting to the rise of the Cloud but is slowly trying to catch up.

#### WaveFront

Wavefront is a cutting edge monitoring service funded by great software engineers who’ve built monitoring tools for the best tech companies in Silicon Valley. The idea is to be able to analyze anything that can produce data points. A query language that looks like SQL allows users to apply mathematical operations to these data points to extract values or detect anomalies from the time series data. While it takes some time to get used to the tool, it’s the type of monitoring that the best companies are using. To my knowledge, LinkedIn, Facebook and DropBox are using a very similar tool for their monitoring needs.

-   [Server]()

Servers are located in datacenters which are buildings that host hundreds, or even thousands of computers (servers). You can think of a server as a computer without a keyboard, mouse, or screen, that is accessible only by a network. A server can be physical or virtual. A server runs an OS (operating system).

-   [What is a server](https://en.wikipedia.org/wiki/Server_(computing)#Hardware_requirement)

Watch:

-   [What is a server](https://intranet.alxswe.com/rltoken/miEIK3vwQRPRIPiPyBXn3A)
-   [Where are servers hosted (data centers)](https://www.youtube.com/watch?t=33&v=iuqXFC_qIvA&feature=youtu.be)

Do not mix up  **server**  and  **web server**. (Check out the  **web server**  concept page to know more about this.)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/hb3pAsO.png)

## Background Context

“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

-   Application monitoring: getting data about your running software and making sure it is behaving as expected
-   Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/ktCXnhE.jpg)

## Resources

**Read or watch**:

-   [What is server monitoring](https://www.sumologic.com/glossary/server-monitoring/)
-   [What is application monitoring](https://en.wikipedia.org/wiki/Application_performance_management)
-   [System monitoring by Google](https://sre.google/sre-book/monitoring-distributed-systems/)
-   [Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)




### [0. Sign up for Datadog and install datadog-agent](https://github.com/vpnchengo/alx-system_engineering-devops/blob/master/0x18-webstack_monitoring/2-setup_datadog)

For this task head to  [https://www.datadoghq.com/](https://www.datadoghq.com/)  and sign up for a free  `Datadog`  account. When signing up, you’ll have the option of selecting statistics from your current stack that  `Datadog`  can monitor for you. Once you have an account set up, follow the instructions given on the website to install the  `Datadog`  agent.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6b0ea6345a6375437845.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230607%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230607T045825Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3495b7a2222eb62385f87950fb7127b6142bc0b5290c6458d4b568172cabc92a)

-   Sign up for Datadog -  **Please make sure you are using the US website of Datagog (.com)**
-   Install  `datadog-agent`  on  `web-01`
-   Create an  `application key`
-   Copy-paste in your Intranet user profile ([here](https://intranet.alxswe.com/rltoken/elXu5CcaGpeK7GxerBb7wQ "here")) your DataDog  `API key`  and your DataDog  `application key`.
-   Your server  `web-01`  should be visible in Datadog under the host name  `XX-web-01`
    -   You can validate it by using this  [API](https://docs.datadoghq.com/api/latest/hosts/)
    -   If needed, you will need to update the hostname of your server


### 1.  [Monitor some metrics](https://github.com/vpnchengo/alx-system_engineering-devops/blob/master/0x18-webstack_monitoring)

Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some  `monitors`  within the  `Datadog`  dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here:  [System Check](https://docs.datadoghq.com/integrations/system/).

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6a4551974aadc181e97a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230607%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230607T045825Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8282332a4b8222a44edd168a2f5d9de91ac0ec3dbb353fa59d529c5a25ebf0ca)

-   Set up a monitor that checks the number of read requests issued to the device per second.
-   Set up a monitor that checks the number of write requests issued to the device per second.


### 2.  [Create a dashboard](https://github.com/vpnchengo/alx-system_engineering-devops/blob/master/0x18-webstack_monitoring/2-setup_datadog)

Now create a dashboard with different metrics displayed in order to get a few different visualizations.

-   Create a new  `dashboard`
-   Add at least 4  `widgets`  to your dashboard. They can be of any type and monitor whatever you’d like
-   Create the answer file  `2-setup_datadog`  which has the  `dashboard_id`  on the first line.  **Note**: in order to get the id of your dashboard, you may need to use  [Datadog’s API](https://docs.datadoghq.com/api/?lang=python#get-all-dashboards)

---
## [](https://github.com/vpnchengo/alx-system_engineering-devops#authors) Authors

-   [Alvin](https://github.com/vpnchengo)



