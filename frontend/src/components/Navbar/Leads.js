import React, { Component } from 'react';  
import ReactTable from "react-table-6";  
    import "react-table-6/react-table.css"   
class Leads extends Component {  
  render() {  
        const data = [{  
            name: 'Ayaan',  
            age: 26,
            code:10,
            phonenumber:7419638521,
            city:'Sydney',
            Country:'Australia',  
            },{  
            name: 'Ahana',  
            age: 22,
            
            code:11,
            phonenumber:9637411021,
            city:'Nashik',
            Country:'India',  
            },{  
            name: 'Peter',  
            age: 40,
            
            code:12,
            phonenumber:7418529630,
            city:'Kolkata',
            Country:'India',      
            },{  
            name: 'Virat',  
            age: 30,
            
            code:13,
            phonenumber: 4749651741,
            city:'NJ',
            Country:'USA',  
            },{  
            name: 'Rohit',  
            age: 32,
            code:13,
            phonenumber:7417418963,
            city: 'Mumbai',
            Country:'Inida',  
            },{  
            name: 'Dhoni',  
            age: 37,
            code:14,
            phonenumber:8779143651,
            city:'Pune',
            Country:'India',  
            }]  
        const columns = [{  
        Header: 'Name',  
        accessor: 'name'  
        },{  
        Header: 'Age',  
        accessor: 'age'  
        },{  
            Header: 'Code',  
            accessor: 'code'  
            },
            {  
                Header: 'Contact-Number',  
                accessor: 'phonenumber'  
                },
                {  
                    Header: 'city',  
                    accessor: 'city'  
                    },
                    {  
                        Header: 'country',  
                        accessor: 'Country'  
                        },
        ]  
        return (  
            <div>  
                <ReactTable  
                    data={data}  
                    columns={columns}  
                    defaultPageSize = {2}  
                    pageSizeOptions = {[2,4, 6]}  
                />  
            </div>        
        )  
  }  
}  
export default Leads;