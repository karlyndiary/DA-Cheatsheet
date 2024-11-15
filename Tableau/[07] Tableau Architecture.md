- 4 Layers
  - Source
    - Data could be in MySQL, Oracle, Excel, JSON, API or Cloud. Data could be anywhere.
  - Desktop
    The first thing to do in Tableau Desktop is connect to the Data Source
    - Data Connectors
      - 90 Connectors
    - Access Information will be stored inside the data source
      - Path of the file
      - Access Token
      - Database location
      - Username and password and more
    - Connection Type
      - Extract
      - Live
    - Data Model
      - Join tables together using joins, relationships and unions.
    - Visualizations
      - Tableau organizes the viz in three levels
        - Worksheets: These worksheets can also be created using two data sources[Extract and live] together called Data Blending
  - Server
    - 
  - Consumer
    - Workbook to consumers: .twbx
    - Workbook to Dev Team: .hyper, .tdsx, .twbx, .tds, .twb

  - Server Publish
    - The workbook with the extracted data to be published is sent to the gateway as a .twbx file, which contains both the data and the associated XML metadata.
    - This .twbx file is transmitted to the application server.
    - The XML file within the workbook stores the metadata of the workbook and is then sent to the repository.
    - The .hyper file, which contains the actual data, is sent to the file store for storage.

  - Authentication Process
    - The user logs into the system using their username and password.
    - This action sends a login request to the authentication server.
    - The authentication server checks the selected repository to verify if the user has permission to access the requested file.

  - Access View Process
    - User Login: The user accesses Tableau Server via a web browser and enters their login credentials (username and password).
    - Authentication: The credentials are sent to the authentication server, which verifies the user’s identity using a specified method (e.g., Active Directory, SAML, or local authentication).
    - Authorization Check: Once authenticated, the server checks the user's permissions in the repository to determine access rights for specific workbooks, data sources, or dashboards.
    - Access Granted: If authorized, the user can access and interact with approved content on Tableau Server based on their permission level (such as viewer, editor, or admin).
    - Session Management: Tableau Server manages the user session, ensuring secure access and compliance with additional security protocols during the session.

    - Process: Tableau Server Workflow for Visualizations
      - Signal from Tableau Server: The Tableau Server receives a signal indicating a request for a visualization. The signal is sent to the Application Server, which manages user sessions and permissions.
      
      - Forward to VizQL Server: Since the request pertains to a visualization, the Application Server forwards it to the VizQL Server. The VizQL Server is responsible for handling queries related to visualizations.
      
      - Permission Check: The VizQL Server checks with the Repository (PostgreSQL database used by Tableau) to verify if the user has permission to access the requested visualization.    
      If the user is authorized, the Repository responds with an "OK."
      If not, the request is denied.

      - Request for Dashboard File (TWB or TWBX): Upon receiving approval, the VizQL Server requests the Repository for the XML file of the dashboard (.TWB) or the packaged workbook (.TWBX). These files contain the structure and metadata of the dashboard but not the data itself.
      
      - Dashboard Rendering Initialization: The VizQL Server begins building the visualization framework based on the retrieved file. At this stage, Tableau is aware of the data requirements to complete the visualization.
      
      - Data Request to Data Server: The VizQL Server sends a request to the Data Server to fetch the required data for rendering the dashboard.
      
      - Querying the Data Engine: The Data Server communicates with the Data Engine (Hyper or legacy Tableau Data Engine) to process the request.     
      The Data Engine queries the File Store (Tableau’s storage system for extracts) or the external data source if the data is not stored locally.
      - Data Retrieval from File Store or Data Source: The File Store (or external database) sends the requested data back to the Data Engine, which processes it as per the query logic.
      
      - Data Transfer to VizQL Server: The processed data is sent from the Data Engine to the Data Server, and then to the VizQL Server for integration with the visualization framework.
      
      - Final Dashboard Rendering: The VizQL Server combines the data with the visualization structure (defined in the TWB/TWBX file) and renders the final dashboard. This rendered visualization is displayed to the user via their browser or Tableau Desktop.

- Application Server: It handles Authentication and Authorisation, Publishing and UI Rendering.
- VisQL Server [Visual Query Language]: For example, when you drag a measure and dimension in tableau -> VisQL now converts this to SQL query -> and sends it to the data server to get the data -> The data server sends the raw data to VisQL -> Now VisQL will now translate it to visual.
- Data Server: Knows everything about the data, knows where to find the data, how to connect it and how to speak to it. 
