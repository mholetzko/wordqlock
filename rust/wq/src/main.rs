
use std::time::{Instant};
use chrono::prelude::*;


struct Time2IndexCfg {
    repr_str: String,
    repr_num: u8,
    sign_in_count: [(u8,u8);12]
}


struct TimeLayout {
    min_cfg : [Time2IndexCfg;13],
    hour_cfg : [Time2IndexCfg;12]

}

impl TimeLayout {
    fn new() -> TimeLayout {
        TimeLayout {
            
            min_cfg :[ Time2IndexCfg { repr_str:String::from("VOLL     "    ),repr_num:0 ,sign_in_count:[(9,8),(9,9),(9,10),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] },
                       Time2IndexCfg { repr_str:String::from("FUENFNACH"    ),repr_num:5 ,sign_in_count:[(0,7),(0,8),(0,9),(0,10),(3,7),(3,8),(3,9),(3,10),(99,99),(99,99),(99,99),(99,99)] }, 
                       Time2IndexCfg { repr_str:String::from("ZEHNNACH"     ),repr_num:10,sign_in_count:[(1,0),(1,1),(1,2),(1,3),(3,7),(3,8),(3,9),(3,10),(99,99),(99,99),(99,99),(99,99)] },
                       Time2IndexCfg { repr_str:String::from("VIERTELNACH"  ),repr_num:15,sign_in_count:[(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(3,7),(3,8),(3,9),(3,10),(99,99)] }, 
                       Time2IndexCfg { repr_str:String::from("ZWANZIGNACH"  ),repr_num:20,sign_in_count:[(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(3,7),(3,8),(3,9),(3,10),(99,99)] },
                       Time2IndexCfg { repr_str:String::from("FUNFVORHALB"  ),repr_num:25,sign_in_count:[(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(4,3),(0,7),(0,8),(0,9),(0,10),(99,99)] }, 
                       Time2IndexCfg { repr_str:String::from("HALB"         ),repr_num:30,sign_in_count:[(4,0),(4,1),(4,2),(4,3),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] }, 
                       Time2IndexCfg { repr_str:String::from("FUNEFNACHHALB"),repr_num:35,sign_in_count:[(0,7),(0,8),(0,9),(0,10),(4,0),(4,1),(4,2),(4,3),(3,7),(3,8),(3,9),(3,10)]}, 
                       Time2IndexCfg { repr_str:String::from("ZWANZIGVOR"   ),repr_num:40,sign_in_count:[(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(3,0),(3,1),(3,2),(99,99),(99,99)] }, 
                       Time2IndexCfg { repr_str:String::from("VIERTELVOR"   ),repr_num:45,sign_in_count:[(2,4),(2,5),(2,6),(2,7),(2,8),(2,9),(2,10),(3,0),(3,1),(3,2),(99,99),(99,99)] } ,
                       Time2IndexCfg { repr_str:String::from("ZEHNVOR"      ),repr_num:50,sign_in_count:[(1,0),(1,1),(1,2),(1,3),(3,0),(3,1),(3,2),(1,10),(3,0),(3,1),(3,2),(99,99)] }, 
                       Time2IndexCfg { repr_str:String::from("FUENFVOR"     ),repr_num:55,sign_in_count:[(3,0),(3,1),(3,2),(0,7),(0,8),(0,9),(0,10),(1,10),(3,0),(3,1),(3,2),(99,99)] }, 
                       Time2IndexCfg { repr_str:String::from("VOLL    "     ),repr_num:60,sign_in_count:[(9,8),(9,9),(9,10),(1,7),(1,8),(1,9),(1,10),(3,0),(3,1),(3,2),(99,99),(99,99)] }  ],
        
            hour_cfg : [ Time2IndexCfg { repr_str:String::from("ZWOLF" ),repr_num:0 ,sign_in_count:[(8,6),(8,7),(8,8),(8,9),(8,10),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] },
                         Time2IndexCfg { repr_str:String::from("EINS"  ),repr_num:1 ,sign_in_count:[(5,0),(5,1),(5,2),(5,3),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] }, 
                         Time2IndexCfg { repr_str:String::from("ZWEI"  ),repr_num:2,sign_in_count:[(5,7),(5,8),(5,9),(5,10),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] },
                         Time2IndexCfg { repr_str:String::from("DREI"  ),repr_num:3,sign_in_count:[(6,0),(6,1),(6,2),(6,3),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] }, 
                         Time2IndexCfg { repr_str:String::from("VIER"  ),repr_num:4,sign_in_count:[(6,7),(6,8),(6,9),(6,10),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] },
                         Time2IndexCfg { repr_str:String::from("FUNF"  ),repr_num:5,sign_in_count:[(4,7),(4,8),(4,9),(4,10),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] }, 
                         Time2IndexCfg { repr_str:String::from("SECHS" ),repr_num:6,sign_in_count:[(7,0),(7,1),(7,2),(7,3),(7,4),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] }, 
                         Time2IndexCfg { repr_str:String::from("SIEBEN"),repr_num:7,sign_in_count:[(8,0),(8,1),(8,2),(8,3),(8,4),(8,5),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)]}, 
                         Time2IndexCfg { repr_str:String::from("ACHT"  ),repr_num:8,sign_in_count:[(7,7),(7,8),(7,9),(7,10),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] }, 
                         Time2IndexCfg { repr_str:String::from("NEUN"  ),repr_num:9,sign_in_count:[(9,3),(9,4),(9,5),(9,6),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] } ,
                         Time2IndexCfg { repr_str:String::from("ZEHN"  ),repr_num:10,sign_in_count:[(9,0),(9,1),(9,2),(9,3),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] }, 
                         Time2IndexCfg { repr_str:String::from("ELF"   ),repr_num:11,sign_in_count:[(4,5),(4,6),(4,7),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99),(99,99)] },  ]
        }
    }
}

struct TimeHandler {
    current_time : DateTime<Local> 
}

impl TimeHandler {

    fn update_time(&mut self) {
        self.current_time = Local::now();
    }

    fn get_table_time(&mut self) {

    }

    fn get_current_min_cfg(&mut self) {

    }

    fn get_current_hour_cfg(&mut self) {
        
    }

    fn get_current_min_offset(&mut self) {

    }

    fn get_current_second_offset(&mut self) {

    }
}



fn main() {
    println!("wqSimulation entry point");
    
    let mut now = Instant::now();
    let interval = 5;

    let letter_field = [["E","S","K","I","S","T","A","F","Ü","N","F"],
                        ["Z","E","H","N","Z","W","A","N","Z","I","G"],
                        ["D","R","E","I","V","I","E","R","T","E","L"],
                        ["V","O","R","F","U","N","K","N","A","C","H"],
                        ["H","A","L","B","A","E","L","F","U","N","F"],
                        ["E","I","N","S","X","A","M","Z","W","E","I"],
                        ["D","R","E","I","P","M","J","V","I","E","R"],
                        ["S","E","C","H","S","B","L","A","C","H","T"],
                        ["S","I","E","B","E","N","Z","W","Ö","L","F"],
                        ["Z","E","H","N","E","U","N","K","U","H","R"]];

    let static_indices = [(0,0),(0,1),(0,3),(0,4),(0,5)];
    //UHR
    let clock_indices = [(9,8),(9,9),(9,10)];
    //AM
    let am_indices     = [(5,5),(6,5)];
    //PM
    let pm_indices     = [(6,4),(6,5)];

    let mut time_layout = TimeLayout::new();

    loop {
        //Read Time
        if now.elapsed().as_secs() > interval
        {
            //Update cycles are 
            println!("Another 5s wasted");
            now = Instant::now();


            //Update Time

            //Set Bitmaps
        }

    }
}
