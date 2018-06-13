all_k_type = ['1min', '3min', '5min', '10min',
              '30min', '1day']
all_ex_sy = {
    "okex":"ltc_btc,eth_btc,etc_btc,bch_btc,btc_usdt,eth_usdt,ltc_usdt,etc_usdt,bch_usdt,etc_eth,btg_btc,qtum_btc,hsr_btc,neo_btc,gas_btc,qtum_usdt,hsr_usdt,neo_usdt,gas_usdt,xrp_btc,xem_btc,xlm_btc,iota_btc,1st_btc,aac_btc,ace_btc,act_btc,aidoc_btc,amm_btc,ark_btc,ast_btc,atl_btc,avt_btc,bcd_btc,bcx_btc,bec_btc,bnt_btc,brd_btc,bt2_btc,btm_btc,cag_btc,can_btc,cbt_btc,chat_btc,cic_btc,cmt_btc,ctr_btc,cvc_btc,dash_btc,dat_btc,dent_btc,dgb_btc,dgd_btc,dna_btc,dnt_btc,dpy_btc,edo_btc,elf_btc,eng_btc,eos_btc,evx_btc,fair_btc,fun_btc,gnt_btc,gnx_btc,gto_btc,hmc_btc,hot_btc,icn_btc,icx_btc,ins_btc,insur_btc,int_btc,iost_btc,ipc_btc,itc_btc,kcash_btc,key_btc,knc_btc,la_btc,lend_btc,lev_btc,light_btc,link_btc,lrc_btc,mag_btc,mana_btc,mco_btc,mda_btc,mdt_btc,mkr_btc,mof_btc,mot_btc,mth_btc,mtl_btc,nano_btc,nas_btc,ngc_btc,nuls_btc,oax_btc,of_btc,omg_btc,ost_btc,pay_btc,poe_btc,ppt_btc,pra_btc,pst_btc,qun_btc,qvt_btc,r_btc,rcn_btc,rct_btc,rdn_btc,read_btc,ref_btc,req_btc,rnt_btc,salt_btc,san_btc,sbtc_btc,show_btc,smt_btc,snc_btc,sngls_btc,snm_btc,snt_btc,soc_btc,spf_btc,ssc_btc,stc_btc,storj_btc,sub_btc,swftc_btc,tct_btc,theta_btc,tio_btc,tnb_btc,topc_btc,true_btc,trx_btc,ubtc_btc,uct_btc,ugc_btc,ukg_btc,utk_btc,vee_btc,vib_btc,viu_btc,wbtc_btc,wrc_btc,wtc_btc,xmr_btc,xuc_btc,yee_btc,yoyo_btc,zec_btc,zen_btc,zip_btc,zrx_btc,xrp_usdt,xem_usdt,xlm_usdt,iota_usdt,1st_usdt,aac_usdt,ace_usdt,act_usdt,aidoc_usdt,amm_usdt,ark_usdt,ast_usdt,atl_usdt,avt_usdt,bcd_usdt,bec_usdt,bnt_usdt,brd_usdt,btg_usdt,btm_usdt,cag_usdt,can_usdt,cbt_usdt,chat_usdt,cic_usdt,cmt_usdt,ctr_usdt,cvc_usdt,dash_usdt,dat_usdt,dent_usdt,dgb_usdt,dgd_usdt,dna_usdt,dnt_usdt,dpy_usdt,edo_usdt,elf_usdt,eng_usdt,eos_usdt,evx_usdt,fair_usdt,fun_usdt,gnt_usdt,gnx_usdt,gto_usdt,hmc_usdt,hot_usdt,icn_usdt,icx_usdt,ins_usdt,insur_usdt,int_usdt,iost_usdt,ipc_usdt,itc_usdt,kcash_usdt,key_usdt,knc_usdt,la_usdt,lend_usdt,lev_usdt,light_usdt,link_usdt,lrc_usdt,mag_usdt,mana_usdt,mco_usdt,mda_usdt,mdt_usdt,mkr_usdt,mof_usdt,mot_usdt,mth_usdt,mtl_usdt,nano_usdt,nas_usdt,ngc_usdt,nuls_usdt,oax_usdt,of_usdt,omg_usdt,ost_usdt,pay_usdt,poe_usdt,ppt_usdt,pra_usdt,pst_usdt,qun_usdt,qvt_usdt,r_usdt,rcn_usdt,rct_usdt,rdn_usdt,read_usdt,ref_usdt,req_usdt,rnt_usdt,salt_usdt,san_usdt,show_usdt,smt_usdt,snc_usdt,sngls_usdt,snm_usdt,snt_usdt,soc_usdt,spf_usdt,ssc_usdt,stc_usdt,storj_usdt,sub_usdt,swftc_usdt,tct_usdt,theta_usdt,tio_usdt,tnb_usdt,topc_usdt,true_usdt,trx_usdt,ubtc_usdt,uct_usdt,ugc_usdt,ukg_usdt,utk_usdt,vee_usdt,vib_usdt,viu_usdt,wrc_usdt,wtc_usdt,xmr_usdt,xuc_usdt,yee_usdt,yoyo_usdt,zec_usdt,zen_usdt,zip_usdt,zrx_usdt,ltc_bch,etc_bch,act_bch,avt_bch,bcd_bch,bcx_bch,btg_bch,cmt_bch,dash_bch,dgd_bch,edo_bch,eos_bch,sbtc_bch,ltc_eth,bch_eth,xrp_eth,xem_eth,xlm_eth,iota_eth,1st_eth,aac_eth,ace_eth,act_eth,aidoc_eth,amm_eth,ark_eth,ast_eth,atl_eth,avt_eth,bec_eth,bnt_eth,brd_eth,btm_eth,cag_eth,can_eth,cbt_eth,chat_eth,cic_eth,cmt_eth,ctr_eth,cvc_eth,dash_eth,dat_eth,dent_eth,dgb_eth,dgd_eth,dna_eth,dnt_eth,dpy_eth,edo_eth,elf_eth,eng_eth,eos_eth,evx_eth,fair_eth,fun_eth,gas_eth,gnt_eth,gnx_eth,gto_eth,hmc_eth,hot_eth,hsr_eth,icn_eth,icx_eth,ins_eth,insur_eth,int_eth,iost_eth,ipc_eth,itc_eth,kcash_eth,key_eth,knc_eth,la_eth,lend_eth,lev_eth,light_eth,link_eth,lrc_eth,mag_eth,mana_eth,mco_eth,mda_eth,mdt_eth,mkr_eth,mof_eth,mot_eth,mth_eth,mtl_eth,nano_eth,nas_eth,neo_eth,ngc_eth,nuls_eth,oax_eth,of_eth,omg_eth,ost_eth,pay_eth,poe_eth,ppt_eth,pra_eth,pst_eth,qtum_eth,qun_eth,qvt_eth,r_eth,rcn_eth,rct_eth,rdn_eth,read_eth,ref_eth,req_eth,rnt_eth,salt_eth,san_eth,show_eth,smt_eth,snc_eth,sngls_eth,snm_eth,snt_eth,soc_eth,spf_eth,ssc_eth,stc_eth,storj_eth,sub_eth,swftc_eth,tct_eth,theta_eth,tio_eth,tnb_eth,topc_eth,true_eth,trx_eth,ubtc_eth,uct_eth,ugc_eth,ukg_eth,utk_eth,vee_eth,vib_eth,viu_eth,wrc_eth,wtc_eth,xmr_eth,xuc_eth,yee_eth,yoyo_eth,zec_eth,zen_eth,zip_eth,zrx_eth,mith_btc,mith_usdt,mith_eth,abt_btc,abt_usdt,abt_eth,auto_btc,bkx_btc,gtc_btc,auto_usdt,bkx_usdt,gtc_usdt,auto_eth,bkx_eth,gtc_eth,gsc_btc,rfr_btc,trio_btc,gsc_usdt,rfr_usdt,trio_usdt,gsc_eth,rfr_eth,trio_eth,tra_btc,tra_usdt,tra_eth,ren_btc,wfee_btc,ren_usdt,wfee_usdt,ren_eth,wfee_eth",
    "zb":"btc_usdt,bcc_usdt,ltc_usdt,eth_usdt,etc_usdt,bts_usdt,eos_usdt,qtum_usdt,hsr_usdt,xrp_usdt,bcd_usdt,dash_usdt,bcc_btc,ltc_btc,eth_btc,etc_btc,bts_btc,eos_btc,qtum_btc,hsr_btc,xrp_btc,bcd_btc,dash_btc,bat_usdt,sbtc_btc,ubtc_usdt,bcw_usdt,chat_btc,ink_btc,sbtc_usdt,topc_btc,qun_usdt,btp_btc,tv_btc,qun_btc,bth_btc,1st_usdt,btn_usdt,true_btc,topc_usdt,ddm_btc,safe_usdt,lbtc_usdt,bite_btc,hlc_usdt,bat_btc,lbtc_btc,ink_usdt,chat_usdt,cdc_usdt,ubtc_btc,cdc_btc,ent_usdt,bth_usdt,ddm_usdt,hlc_btc,1st_btc,bcx_btc,btp_usdt,bcw_btc,ent_btc,bcx_usdt,safe_btc,true_usdt,tv_usdt,btn_btc,hotc_btc,hotc_usdt,epc_btc,xuc_btc,qc_usdt,bds_btc,zb_usdt,zb_btc,gram_btc,gram_usdt",
    "huobi":"act_btc,act_eth,aidoc_btc,aidoc_eth,ast_btc,bat_btc,bat_eth,bcd_btc,bch_btc,bch_usdt,bcx_btc,bifi_btc,btc_usdt,btg_btc,btm_btc,btm_eth,cmt_btc,cmt_eth,cvc_btc,cvc_eth,cvc_usdt,dash_btc,dash_usdt,dbc_btc,dbc_eth,dgd_btc,dgd_eth,elf_btc,elf_eth,eos_btc,eos_eth,eos_usdt,etc_btc,etc_usdt,eth_btc,eth_usdt,gas_btc,gas_eth,gnt_btc,gnt_eth,gnt_usdt,gnx_btc,gnx_eth,hsr_btc,hsr_eth,hsr_usdt,icx_btc,icx_eth,itc_btc,itc_eth,knc_btc,ltc_btc,ltc_usdt,mana_btc,mana_eth,mco_btc,mco_eth,mds_btc,mds_eth,mtl_btc,nas_btc,nas_eth,neo_btc,neo_usdt,omg_btc,omg_eth,omg_usdt,ost_btc,ost_eth,pay_btc,pay_eth,powr_btc,powr_eth,propy_btc,propy_eth,qash_btc,qash_eth,qsp_btc,qsp_eth,qtum_btc,qtum_eth,qtum_usdt,qun_btc,qun_eth,rcn_btc,rcn_eth,rdn_btc,rdn_eth,req_btc,req_eth,rpx_btc,salt_btc,salt_eth,sbtc_btc,smt_btc,smt_eth,snt_btc,snt_usdt,storj_btc,storj_usdt,swftc_btc,swftc_eth,tnb_btc,tnb_eth,tnt_btc,tnt_eth,topc_btc,topc_eth,ven_btc,ven_eth,wax_btc,wax_eth,wicc_btc,wicc_eth,xrp_btc,xrp_usdt,zec_btc,zec_usdt,zrx_btc,link_btc,evx_btc,iost_eth,theta_btc,dat_btc,chat_eth,smt_usdt,let_btc,utk_btc,bt2_btc,dta_eth,mee_eth,adx_eth,eko_eth,eko_btc,appc_btc,dat_eth,iost_usdt,dta_btc,mee_btc,link_eth,iost_btc,yee_btc,let_eth,evx_eth,theta_eth,ven_usdt,adx_btc,xem_btc,chat_btc,bt1_btc,utk_eth,appc_eth,yee_eth,xem_usdt,ruff_eth,soc_eth,soc_btc,zil_btc,ruff_btc,zil_eth,elf_usdt,lun_eth,lun_btc,ocn_eth,ocn_btc,trx_eth,trx_btc,theta_usdt,ela_eth,ht_btc,let_usdt,srn_btc,stk_eth,ht_eth,ht_usdt,ela_btc,srn_eth,stk_btc,zla_eth,zla_btc,dta_usdt,snc_btc,lsk_btc,mtn_eth,snc_eth,lsk_eth,mtn_btc,mtx_btc,mtx_eth,zil_usdt,wpr_btc,wpr_eth,ruff_usdt,nas_usdt,itc_usdt,eng_eth,eng_btc,blz_eth,edu_btc,edu_eth,blz_btc,abt_eth,abt_btc,ela_usdt,ont_btc,mds_usdt,ont_eth,trx_usdt",
    "binance":"eth_btc,ltc_btc,bnb_btc,neo_btc,qtum_eth,eos_eth,snt_eth,bnt_eth,bcc_btc,gas_btc,bnb_eth,btc_usdt,eth_usdt,hsr_btc,oax_eth,dnt_eth,mco_eth,icn_eth,mco_btc,wtc_btc,wtc_eth,lrc_btc,lrc_eth,qtum_btc,yoyo_btc,omg_btc,omg_eth,zrx_btc,zrx_eth,strat_btc,strat_eth,sngls_btc,sngls_eth,bqx_btc,bqx_eth,knc_btc,knc_eth,fun_btc,fun_eth,snm_btc,snm_eth,neo_eth,iota_btc,iota_eth,link_btc,link_eth,xvg_btc,xvg_eth,ctr_btc,ctr_eth,salt_btc,salt_eth,mda_btc,mda_eth,mtl_btc,mtl_eth,sub_btc,sub_eth,eos_btc,snt_btc,etc_eth,etc_btc,mth_btc,mth_eth,eng_btc,eng_eth,dnt_btc,zec_btc,zec_eth,bnt_btc,ast_btc,ast_eth,dash_btc,dash_eth,oax_btc,icn_btc,btg_btc,btg_eth,evx_btc,evx_eth,req_btc,req_eth,vib_btc,vib_eth,hsr_eth,trx_btc,trx_eth,powr_btc,powr_eth,ark_btc,ark_eth,yoyo_eth,xrp_btc,xrp_eth,mod_btc,mod_eth,enj_btc,enj_eth,storj_btc,storj_eth,bnb_usdt,ven_bnb,yoyo_bnb,powr_bnb,ven_btc,ven_eth,kmd_btc,kmd_eth,nuls_bnb,rcn_btc,rcn_eth,rcn_bnb,nuls_btc,nuls_eth,rdn_btc,rdn_eth,rdn_bnb,xmr_btc,xmr_eth,dlt_bnb,wtc_bnb,dlt_btc,dlt_eth,amb_btc,amb_eth,amb_bnb,bcc_eth,bcc_usdt,bcc_bnb,bat_btc,bat_eth,bat_bnb,bcpt_btc,bcpt_eth,bcpt_bnb,arn_btc,arn_eth,gvt_btc,gvt_eth,cdt_btc,cdt_eth,gxs_btc,gxs_eth,neo_usdt,neo_bnb,poe_btc,poe_eth,qsp_btc,qsp_eth,qsp_bnb,bts_btc,bts_eth,bts_bnb,xzc_btc,xzc_eth,xzc_bnb,lsk_btc,lsk_eth,lsk_bnb,tnt_btc,tnt_eth,fuel_btc,fuel_eth,mana_btc,mana_eth,bcd_btc,bcd_eth,dgd_btc,dgd_eth,iota_bnb,adx_btc,adx_eth,adx_bnb,ada_btc,ada_eth,ppt_btc,ppt_eth,cmt_btc,cmt_eth,cmt_bnb,xlm_btc,xlm_eth,xlm_bnb,cnd_btc,cnd_eth,cnd_bnb,lend_btc,lend_eth,lend_bnb,wabi_btc,wabi_eth,wabi_bnb,ltc_eth,ltc_usdt,ltc_bnb,tnb_btc,tnb_eth,waves_btc,waves_eth,waves_bnb,gto_btc,gto_eth,gto_bnb,icx_btc,icx_eth,icx_bnb,ost_btc,ost_eth,ost_bnb,elf_btc,elf_eth,aion_btc,aion_eth,aion_bnb,nebl_btc,nebl_eth,nebl_bnb,brd_btc,brd_eth,brd_bnb,mco_bnb,edo_btc,edo_eth,wings_btc,wings_eth,nav_btc,nav_eth,nav_bnb,lun_btc,lun_eth,trig_btc,trig_eth,trig_bnb,appc_btc,appc_eth,appc_bnb,vibe_btc,vibe_eth,rlc_btc,rlc_eth,rlc_bnb,ins_btc,ins_eth,pivx_btc,pivx_eth,pivx_bnb,iost_btc,iost_eth,chat_btc,chat_eth,steem_btc,steem_eth,steem_bnb,xrb_btc,xrb_eth,xrb_bnb,via_btc,via_eth,via_bnb,blz_btc,blz_eth,blz_bnb,ae_btc,ae_eth,ae_bnb,rpx_btc,rpx_eth,rpx_bnb,ncash_btc,ncash_eth,ncash_bnb,poa_btc,poa_eth,poa_bnb,zil_btc,zil_eth,zil_bnb,ont_btc,nt_eth,ont_bnb,storm_btc,storm_eth,storm_bnb",
    "bitfinex":"btc_usd,ltc_usd,ltc_btc,eth_usd,eth_btc,etc_btc,etc_usd,zec_usd,zec_btc,xmr_usd,xmr_btc,bcc_btc,bcc_usd,btc_eur,xrp_usd,xrp_btc,iot_usd,iot_btc,iot_eth,eos_usd,eos_btc,eos_eth,omg_usd,omg_btc,omg_eth,bch_usd,bch_btc,bch_eth,neo_usd,neo_btc,neo_eth,etp_usd,etp_btc,etp_eth,edo_usd,edo_btc,edo_eth,btg_usd,btg_btc,qsh_usd,qsh_btc,qsh_eth,rrt_usd,rrt_btc,dsh_usd,dsh_btc,san_usd,san_btc,san_eth,qtm_usd,qtm_btc,qtm_eth,avt_usd,avt_btc,avt_eth,dat_usd,dat_btc,dat_eth,yyw_usd,yyw_btc,yyw_eth,gnt_usd,gnt_btc,gnt_eth,snt_usd,snt_btc,snt_eth,iot_eur,bat_usd,bat_btc,bat_eth,mna_usd,mna_btc,mna_eth,fun_usd,fun_btc,fun_eth,zrx_usd,zrx_btc,zrx_eth,tnb_usd,tnb_btc,tnb_eth,spk_usd,spk_btc,spk_eth,trx_usd,trx_btc,trx_eth,rcn_usd,rcn_btc,rcn_eth,rlc_usd,rlc_btc,rlc_eth,aid_usd,aid_btc,aid_eth,sng_usd,sng_btc,sng_eth,rep_usd,rep_btc,rep_eth,elf_usd,elf_btc,elf_eth",
    "bithumb":"btc_krw,eth_krw,dash_krw,ltc_krw,etc_krw,xrp_krw,bch_krw,xmr_krw,zec_krw,qtum_krw,btg_krw,eos_krw",
    "bitstamp":"btc_usd,xrp_usd,ltc_usd,eth_usd,btc_eur,eth_eur,eth_btc,ltc_eur,ltc_btc,xrp_eur,xrp_btc,bch_usd,bch_eur,bch_btc",
    "bitstar":"btc_usd,eth_usd,etc_usd,ltc_usd,bch_usd",
    "bittrex":"1st_btc,2give_btc,aby_btc,ada_btc,adt_btc,adx_btc,aeon_btc,agrs_btc,amp_btc,ant_btc,apx_btc,ardr_btc,ark_btc,aur_btc,bat_btc,bay_btc,bcc_btc,bcy_btc,bitb_btc,blitz_btc,blk_btc,block_btc,bnt_btc,brk_btc,brx_btc,bsd_btc,btcd_btc,btg_btc,burst_btc,byc_btc,cann_btc,cfi_btc,clam_btc,cloak_btc,club_btc,coval_btc,cpc_btc,crb_btc,crw_btc,cure_btc,cvc_btc,dash_btc,dcr_btc,dct_btc,dgb_btc,dgd_btc,dmd_btc,dnt_btc,doge_btc,dope_btc,dtb_btc,dyn_btc,ebst_btc,edg_btc,efl_btc,egc_btc,emc_btc,emc2_btc,eng_btc,enrg_btc,erc_btc,etc_btc,eth_btc,excl_btc,exp_btc,fair_btc,fct_btc,fldc_btc,flo_btc,ftc_btc,fun_btc,gam_btc,game_btc,gbg_btc,gbyte_btc,gcr_btc,geo_btc,gld_btc,gno_btc,gnt_btc,golos_btc,grc_btc,grs_btc,gup_btc,hmq_btc,incnt_btc,infx_btc,ioc_btc,ion_btc,iop_btc,kmd_btc,kore_btc,lbc_btc,lgd_btc,lmc_btc,lsk_btc,ltc_btc,lun_btc,maid_btc,mana_btc,mco_btc,meme_btc,mer_btc,mln_btc,mona_btc,mtl_btc,mue_btc,music_btc,myst_btc,nav_btc,nbt_btc,neo_btc,neos_btc,nlg_btc,nmr_btc,nxc_btc,nxs_btc,nxt_btc,ok_btc,omg_btc,omni_btc,part_btc,pay_btc,pdc_btc,pink_btc,pivx_btc,pkb_btc,pot_btc,powr_btc,ppc_btc,ptc_btc,ptoy_btc,qrl_btc,qtum_btc,qwark_btc,rads_btc,rby_btc,rcn_btc,rdd_btc,rep_btc,rise_btc,rlc_btc,salt_btc,sbd_btc,sc_btc,seq_btc,shift_btc,sib_btc,slr_btc,sls_btc,snrg_btc,snt_btc,sphr_btc,spr_btc,start_btc,steem_btc,storj_btc,strat_btc,swift_btc,swt_btc,synx_btc,sys_btc,thc_btc,tix_btc,tks_btc,trig_btc,trst_btc,trust_btc,tx_btc,ubq_btc,unb_btc,via_btc,vib_btc,vox_btc,vrc_btc,vrm_btc,vtc_btc,vtr_btc,waves_btc,wings_btc,xcp_btc,xdn_btc,xel_btc,xem_btc,xlm_btc,xmg_btc,xmr_btc,xmy_btc,xrp_btc,xst_btc,xvc_btc,xvg_btc,xwc_btc,xzc_btc,zcl_btc,zec_btc,zen_btc,1st_eth,ada_eth,adt_eth,adx_eth,ant_eth,bat_eth,bcc_eth,bnt_eth,btg_eth,cfi_eth,crb_eth,cvc_eth,dash_eth,dgb_eth,dgd_eth,dnt_eth,eng_eth,etc_eth,fct_eth,fun_eth,gno_eth,gnt_eth,gup_eth,hmq_eth,lgd_eth,ltc_eth,lun_eth,mana_eth,mco_eth,mtl_eth,myst_eth,neo_eth,nmr_eth,omg_eth,pay_eth,powr_eth,ptoy_eth,qrl_eth,qtum_eth,rcn_eth,rep_eth,rlc_eth,salt_eth,sc_eth,snt_eth,storj_eth,strat_eth,tix_eth,trst_eth,vib_eth,waves_eth,wings_eth,xem_eth,xlm_eth,xmr_eth,xrp_eth,zec_eth,bcc_usdt,btc_usdt,btg_usdt,dash_usdt,etc_usdt,eth_usdt,ltc_usdt,neo_usdt,omg_usdt,xmr_usdt,xrp_usdt,zec_usdt,ukg_btc,ukg_eth,ada_usdt,nxt_usdt,xvg_usdt,ignis_btc,bcpt_btc,srn_btc,vee_btc,wax_btc,zrx_btc,bcpt_eth,srn_eth,vee_eth,wax_eth,zrx_eth,trx_btc,trx_eth,tusd_btc,lrc_btc,lrc_eth,rvr_btc,tusd_eth,up_btc,up_eth",
    "kraken":"xbt_eur,xbt_usd,eth_xbt,bch_xbt,dash_xbt,eos_xbt,etc_xbt,eth_xbt,gno_xbt,icn_xbt,ltc_xbt,mln_xbt,rep_xbt,xbt_cad,xbt_eur,xbt_gbp,xbt_jpy,xbt_usd,xdg_xbt,xlm_xbt,xmr_xbt,xrp_xbt,zec_xbt,bch_eur,bch_usd,bch_xbt,dash_eur,dash_usd,dash_xbt,eos_eth,eos_eur,eos_usd,eos_xbt,etc_eth,etc_eur,etc_usd,etc_xbt,eos_eth,etc_eth,eth_cad,eth_eur,eth_gbp,eth_jpy,eth_usd,eth_xbt,gno_eth,icn_eth,mln_eth,rep_eth,gno_eth,gno_eur,gno_usd,gno_xbt,icn_eth,icn_xbt,ltc_eur,ltc_usd,ltc_xbt,mln_eth,mln_xbt,rep_eth,rep_eur,rep_usd,rep_xbt,usdt_usd,xdg_xbt,xlm_eur,xlm_usd,xlm_xbt,xmr_eur,xmr_usd,xmr_xbt,xrp_cad,xrp_eur,xrp_jpy,xrp_usd,xrp_xbt,zec_eur,zec_jpy,zec_usd,zec_xbt",
    "poloniex":"bcn_btc,bela_btc,blk_btc,btcd_btc,btm_btc,bts_btc,burst_btc,clam_btc,dash_btc,dgb_btc,doge_btc,emc2_btc,fldc_btc,flo_btc,game_btc,grc_btc,huc_btc,ltc_btc,maid_btc,omni_btc,nav_btc,neos_btc,nmc_btc,nxt_btc,pink_btc,pot_btc,ppc_btc,ric_btc,str_btc,sys_btc,via_btc,xvc_btc,vrc_btc,vtc_btc,xbc_btc,xcp_btc,xem_btc,xmr_btc,xpm_btc,xrp_btc,btc_usdt,dash_usdt,ltc_usdt,nxt_usdt,str_usdt,xmr_usdt,xrp_usdt,bcn_xmr,blk_xmr,btcd_xmr,dash_xmr,ltc_xmr,maid_xmr,nxt_xmr,eth_btc,eth_usdt,sc_btc,bcy_btc,exp_btc,fct_btc,rads_btc,amp_btc,dcr_btc,lsk_btc,lsk_eth,lbc_btc,steem_btc,steem_eth,sbd_btc,etc_btc,etc_eth,etc_usdt,rep_btc,rep_usdt,rep_eth,ardr_btc,zec_btc,zec_eth,zec_usdt,zec_xmr,strat_btc,nxc_btc,pasc_btc,gnt_btc,gnt_eth,gno_btc,gno_eth,bch_btc,bch_eth,bch_usdt,zrx_btc,zrx_eth,cvc_btc,cvc_eth,omg_btc,omg_eth,gas_btc,gas_eth,storj_btc"
}
all_exchage = all_ex_sy.keys()