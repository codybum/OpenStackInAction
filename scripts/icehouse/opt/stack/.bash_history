/opt/stack/heat/bin/heat-api-cloudwatch --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-api-cw.pid; fg || echo "h-api-cw failed to start" | tee "/opt/stack/status/stack/h-api-cw.failure"
cd /opt/
cd devstack/
ls -la
more local.conf 
ls -la
./stack.sh
ifconfig -a
sudo shutdown -h now
python /usr/local/bin/neutron-openvswitch-agent --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini & echo $! >/opt/stack/status/stack/q-agt.pid; fg || echo "q-agt failed to start" | tee "/opt/stack/status/stack/q-agt.failure"
/opt/stack/heat/bin/heat-api --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-api.pid; fg || echo "h-api failed to start" | tee "/opt/stack/status/stack/h-api.failure"
/opt/stack/heat/bin/heat-api-cfn --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-api-cfn.pid; fg || echo "h-api-cfn failed to start" | tee "/opt/stack/status/stack/h-api-cfn.failure"
/usr/local/bin/cinder-volume --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-vol.pid; fg || echo "c-vol failed to start" | tee "/opt/stack/status/stack/c-vol.failure"
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-obj.pid; fg || echo "n-obj failed to start" | tee "/opt/stack/status/stack/n-obj.failure"
/usr/local/bin/cinder-api --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-api.pid; fg || echo "c-api failed to start" | tee "/opt/stack/status/stack/c-api.failure"
/usr/local/bin/cinder-scheduler --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-sch.pid; fg || echo "c-sch failed to start" | tee "/opt/stack/status/stack/c-sch.failure"
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-xvnc.pid; fg || echo "n-xvnc failed to start" | tee "/opt/stack/status/stack/n-xvnc.failure"
/usr/local/bin/nova-consoleauth --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-cauth.pid; fg || echo "n-cauth failed to start" | tee "/opt/stack/status/stack/n-cauth.failure"
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC & echo $! >/opt/stack/status/stack/n-novnc.pid; fg || echo "n-novnc failed to start" | tee "/opt/stack/status/stack/n-novnc.failure"
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-sch.pid; fg || echo "n-sch failed to start" | tee "/opt/stack/status/stack/n-sch.failure"
/usr/local/bin/nova-cert --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-crt.pid; fg || echo "n-crt failed to start" | tee "/opt/stack/status/stack/n-crt.failure"
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-cond.pid; fg || echo "n-cond failed to start" | tee "/opt/stack/status/stack/n-cond.failure"
sg libvirtd '/usr/local/bin/nova-compute --config-file /etc/nova/nova.conf' & echo $! >/opt/stack/status/stack/n-cpu.pid; fg || echo "n-cpu failed to start" | tee "/opt/stack/status/stack/n-cpu.failure"
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini & echo $! >/opt/stack/status/stack/q-l3.pid; fg || echo "q-l3 failed to start" | tee "/opt/stack/status/stack/q-l3.failure"
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC & echo $! >/opt/stack/status/stack/n-novnc.pid; fg || echo "n-novnc failed to start" | tee "/opt/stack/status/stack/n-novnc.failure"
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC & echo $! >/opt/stack/status/stack/n-novnc.pid; fg || echo "n-novnc failed to start" | tee "/opt/stack/status/stack/n-novnc.failure"
python /usr/local/bin/neutron-dhcp-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/dhcp_agent.ini & echo $! >/opt/stack/status/stack/q-dhcp.pid; fg || echo "q-dhcp failed to start" | tee "/opt/stack/status/stack/q-dhcp.failure"
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini & echo $! >/opt/stack/status/stack/q-svc.pid; fg || echo "q-svc failed to start" | tee "/opt/stack/status/stack/q-svc.failure"
/usr/local/bin/glance-registry --config-file=/etc/glance/glance-registry.conf & echo $! >/opt/stack/status/stack/g-reg.pid; fg || echo "g-reg failed to start" | tee "/opt/stack/status/stack/g-reg.failure"
sudo tail -f /var/log/apache2/horizon_error.log & echo $! >/opt/stack/status/stack/horizon.pid; fg || echo "horizon failed to start" | tee "/opt/stack/status/stack/horizon.failure"
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug & echo $! >/opt/stack/status/stack/key.pid; fg || echo "key failed to start" | tee "/opt/stack/status/stack/key.failure"
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini & echo $! >/opt/stack/status/stack/q-svc.pid; fg || echo "q-svc failed to start" | tee "/opt/stack/status/stack/q-svc.failure"
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini & echo $! >/opt/stack/status/stack/q-svc.pid; fg || echo "q-svc failed to start" | tee "/opt/stack/status/stack/q-svc.failure"
/usr/local/bin/glance-api --config-file=/etc/glance/glance-api.conf & echo $! >/opt/stack/status/stack/g-api.pid; fg || echo "g-api failed to start" | tee "/opt/stack/status/stack/g-api.failure"
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug & echo $! >/opt/stack/status/stack/key.pid; fg || echo "key failed to start" | tee "/opt/stack/status/stack/key.failure"
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug & echo $! >/opt/stack/status/stack/key.pid; fg || echo "key failed to start" | tee "/opt/stack/status/stack/key.failure"
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-obj.pid; fg || echo "n-obj failed to start" | tee "/opt/stack/status/stack/n-obj.failure"
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-obj.pid; fg || echo "n-obj failed to start" | tee "/opt/stack/status/stack/n-obj.failure"
cd /opt/devstack/
cd ..
ls -la
cd stack/
ls -la
cd ..
cd devstack/
ls -la
more local.conf 
sudo shutdown -h now
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini
exit
/opt/stack/heat/bin/heat-api-cloudwatch --config-file=/etc/heat/heat.conf
exit
cd /opt/
cd devstack/
ls -la
vi local.conf 
./stack.sh
reboot
sudo reboot
sudo vi /etc/sysctl.conf 
sudo sysctl -p
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
ifconfig -a
ifconfig br-ex 172.24.4.250
sudo ifconfig br-ex 172.24.4.250
ping 172.24.4.2
ping 172.24.4.250
iproute
iproute
route
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -t nat 
sudo iptables -t nat list
sudo iptables 
sudo iptables -h
sudo iptables -L
sudo iptables -L nat
sudo iptables nat -L
sudo iptables -L nat
sudo iptables -L 
sudo iptables -L | grep nat
sudo iptables -t nat -A POSTROUTING -o br-ex -j MASQUERADE
sudo tcpdump -i br-ex
pwd
cd ..
ls -la
cd devstack/
ls -la
./unstack.sh
./unstack.sh
./unstack.sh
ls -la
vi local.conf 
/usr/local/bin/glance-registry --config-file=/etc/glance/glance-registry.conf & echo $! >/opt/stack/status/stack/g-reg.pid; fg || echo "g-reg failed to start" | tee "/opt/stack/status/stack/g-reg.failure"
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-obj.pid; fg || echo "n-obj failed to start" | tee "/opt/stack/status/stack/n-obj.failure"
/opt/stack/heat/bin/heat-api-cfn --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-api-cfn.pid; fg || echo "h-api-cfn failed to start" | tee "/opt/stack/status/stack/h-api-cfn.failure"
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-xvnc.pid; fg || echo "n-xvnc failed to start" | tee "/opt/stack/status/stack/n-xvnc.failure"
/opt/stack/cinder/bin/cinder-api --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-api.pid; fg || echo "c-api failed to start" | tee "/opt/stack/status/stack/c-api.failure"
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug & echo $! >/opt/stack/status/stack/key.pid; fg || echo "key failed to start" | tee "/opt/stack/status/stack/key.failure"
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC & echo $! >/opt/stack/status/stack/n-novnc.pid; fg || echo "n-novnc failed to start" | tee "/opt/stack/status/stack/n-novnc.failure"
/opt/stack/heat/bin/heat-api --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-api.pid; fg || echo "h-api failed to start" | tee "/opt/stack/status/stack/h-api.failure"
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini & echo $! >/opt/stack/status/stack/q-svc.pid; fg || echo "q-svc failed to start" | tee "/opt/stack/status/stack/q-svc.failure"
/usr/local/bin/glance-api --config-file=/etc/glance/glance-api.conf & echo $! >/opt/stack/status/stack/g-api.pid; fg || echo "g-api failed to start" | tee "/opt/stack/status/stack/g-api.failure"
python /usr/local/bin/neutron-openvswitch-agent --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini & echo $! >/opt/stack/status/stack/q-agt.pid; fg || echo "q-agt failed to start" | tee "/opt/stack/status/stack/q-agt.failure"
/usr/local/bin/nova-api & echo $! >/opt/stack/status/stack/n-api.pid; fg || echo "n-api failed to start" | tee "/opt/stack/status/stack/n-api.failure"
python /usr/local/bin/neutron-openvswitch-agent --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
sudo /opt/devstack/rejoin-stack.sh
/opt/stack/heat/bin/heat-engine --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-eng.pid; fg || echo "h-eng failed to start" | tee "/opt/stack/status/stack/h-eng.failure"
/opt/stack/cinder/bin/cinder-volume --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-vol.pid; fg || echo "c-vol failed to start" | tee "/opt/stack/status/stack/c-vol.failure"
/opt/stack/cinder/bin/cinder-scheduler --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-sch.pid; fg || echo "c-sch failed to start" | tee "/opt/stack/status/stack/c-sch.failure"
/usr/local/bin/nova-consoleauth --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-cauth.pid; fg || echo "n-cauth failed to start" | tee "/opt/stack/status/stack/n-cauth.failure"
/usr/local/bin/cinder-volume --config-file /etc/cinder/cinder.conf
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-sch.pid; fg || echo "n-sch failed to start" | tee "/opt/stack/status/stack/n-sch.failure"
/usr/local/bin/nova-cert --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-crt.pid; fg || echo "n-crt failed to start" | tee "/opt/stack/status/stack/n-crt.failure"
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-cond.pid; fg || echo "n-cond failed to start" | tee "/opt/stack/status/stack/n-cond.failure"
/opt/stack/cinder/bin/cinder-volume --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-vol.pid; fg || echo "c-vol failed to start" | tee "/opt/stack/status/stack/c-vol.failure"
/opt/stack/cinder/bin/cinder-volume --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-vol.pid; fg || echo "c-vol failed to start" | tee "/opt/stack/status/stack/c-vol.failure"
sg libvirtd '/usr/local/bin/nova-compute --config-file /etc/nova/nova.conf' & echo $! >/opt/stack/status/stack/n-cpu.pid; fg || echo "n-cpu failed to start" | tee "/opt/stack/status/stack/n-cpu.failure"
python /usr/local/bin/neutron-metadata-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/metadata_agent.ini & echo $! >/opt/stack/status/stack/q-meta.pid; fg || echo "q-meta failed to start" | tee "/opt/stack/status/stack/q-meta.failure"
/usr/local/bin/cinder-api --config-file /etc/cinder/cinder.conf
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf
/usr/local/bin/nova-consoleauth --config-file /etc/nova/nova.conf
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini & echo $! >/opt/stack/status/stack/q-l3.pid; fg || echo "q-l3 failed to start" | tee "/opt/stack/status/stack/q-l3.failure"
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC
python /usr/local/bin/neutron-dhcp-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/dhcp_agent.ini & echo $! >/opt/stack/status/stack/q-dhcp.pid; fg || echo "q-dhcp failed to start" | tee "/opt/stack/status/stack/q-dhcp.failure"
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf
/usr/local/bin/nova-cert --config-file /etc/nova/nova.conf
sudo tail -f /var/log/apache2/horizon_error.log & echo $! >/opt/stack/status/stack/horizon.pid; fg || echo "horizon failed to start" | tee "/opt/stack/status/stack/horizon.failure"
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf
python /usr/local/bin/neutron-metadata-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/metadata_agent.ini
/usr/local/bin/nova-compute --config-file /etc/nova/nova.conf
python /usr/local/bin/neutron-dhcp-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/dhcp_agent.ini
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/usr/local/bin/glance-api --config-file=/etc/glance/glance-api.conf
/usr/local/bin/glance-registry --config-file=/etc/glance/glance-registry.conf
sudo tail -f /var/log/apache2/horizon_error.log
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug
ls -la
ls -la
ifconfig -a | more
cd opt
ls -la
cd /opt/
ls -la
cd devstack/
ls -la
ifconfig -a
ping 10.0.2.151
ping 10.0.2.150
ping 10.0.2.151
sudo su -
ls -la
vi local.conf 
./unstack.sh
./unstack.sh
sudo restart
sudo restart
sudo reboot
/opt/stack/heat/bin/heat-api-cloudwatch --config-file=/etc/heat/heat.conf
/opt/stack/heat/bin/heat-api --config-file=/etc/heat/heat.conf
/opt/stack/cinder/bin/cinder-api --config-file /etc/cinder/cinder.conf
/opt/stack/heat/bin/heat-api-cfn --config-file=/etc/heat/heat.conf
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf
python /usr/local/bin/neutron-openvswitch-agent --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/opt/stack/cinder/bin/cinder-volume --config-file /etc/cinder/cinder.conf
/usr/local/bin/nova-consoleauth --config-file /etc/nova/nova.conf
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf
/opt/stack/cinder/bin/cinder-scheduler --config-file /etc/cinder/cinder.conf
/usr/local/bin/nova-cert --config-file /etc/nova/nova.conf
sudo /opt/devstack/rejoin-stack.sh
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf
/usr/local/bin/nova-compute --config-file /etc/nova/nova.conf
python /usr/local/bin/neutron-metadata-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/metadata_agent.ini
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini
python /usr/local/bin/neutron-dhcp-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/dhcp_agent.ini
/usr/local/bin/nova-api
/usr/local/bin/glance-api --config-file=/etc/glance/glance-api.conf
/usr/local/bin/glance-registry --config-file=/etc/glance/glance-registry.conf
sudo tail -f /var/log/apache2/horizon_error.log
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug
cd /opt/devstack/
ls -la
./clean.sh
./clean.sh
sudo reboot
du -h
df -h
cd /opt/devstack/
ls -la
vi local.conf 
ls -la
./stack.sh
ls -la
vi /etc/nova/nova.conf 
ifconfig -a
ifconfig -a | more
sudp reboot
sudo reboot
/opt/stack/heat/bin/heat-api-cloudwatch --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-api-cw.pid; fg || echo "h-api-cw failed to start" | tee "/opt/stack/status/stack/h-api-cw.failure"
python /usr/local/bin/neutron-openvswitch-agent --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini & echo $! >/opt/stack/status/stack/q-agt.pid; fg || echo "q-agt failed to start" | tee "/opt/stack/status/stack/q-agt.failure"
/opt/stack/heat/bin/heat-engine --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-eng.pid; fg || echo "h-eng failed to start" | tee "/opt/stack/status/stack/h-eng.failure"
/opt/stack/heat/bin/heat-api --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-api.pid; fg || echo "h-api failed to start" | tee "/opt/stack/status/stack/h-api.failure"
/opt/stack/cinder/bin/cinder-volume --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-vol.pid; fg || echo "c-vol failed to start" | tee "/opt/stack/status/stack/c-vol.failure"
/opt/stack/cinder/bin/cinder-scheduler --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-sch.pid; fg || echo "c-sch failed to start" | tee "/opt/stack/status/stack/c-sch.failure"
/opt/stack/cinder/bin/cinder-api --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-api.pid; fg || echo "c-api failed to start" | tee "/opt/stack/status/stack/c-api.failure"
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-obj.pid; fg || echo "n-obj failed to start" | tee "/opt/stack/status/stack/n-obj.failure"
/usr/local/bin/nova-consoleauth --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-cauth.pid; fg || echo "n-cauth failed to start" | tee "/opt/stack/status/stack/n-cauth.failure"
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-xvnc.pid; fg || echo "n-xvnc failed to start" | tee "/opt/stack/status/stack/n-xvnc.failure"
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC & echo $! >/opt/stack/status/stack/n-novnc.pid; fg || echo "n-novnc failed to start" | tee "/opt/stack/status/stack/n-novnc.failure"
sg libvirtd '/usr/local/bin/nova-compute --config-file /etc/nova/nova.conf' & echo $! >/opt/stack/status/stack/n-cpu.pid; fg || echo "n-cpu failed to start" | tee "/opt/stack/status/stack/n-cpu.failure"
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-sch.pid; fg || echo "n-sch failed to start" | tee "/opt/stack/status/stack/n-sch.failure"
/usr/local/bin/nova-cert --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-crt.pid; fg || echo "n-crt failed to start" | tee "/opt/stack/status/stack/n-crt.failure"
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-cond.pid; fg || echo "n-cond failed to start" | tee "/opt/stack/status/stack/n-cond.failure"
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini & echo $! >/opt/stack/status/stack/q-l3.pid; fg || echo "q-l3 failed to start" | tee "/opt/stack/status/stack/q-l3.failure"
python /usr/local/bin/neutron-dhcp-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/dhcp_agent.ini & echo $! >/opt/stack/status/stack/q-dhcp.pid; fg || echo "q-dhcp failed to start" | tee "/opt/stack/status/stack/q-dhcp.failure"
/opt/stack/heat/bin/heat-api --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-api.pid; fg || echo "h-api failed to start" | tee "/opt/stack/status/stack/h-api.failure"
/opt/stack/heat/bin/heat-api --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-api.pid; fg || echo "h-api failed to start" | tee "/opt/stack/status/stack/h-api.failure"
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini & echo $! >/opt/stack/status/stack/q-svc.pid; fg || echo "q-svc failed to start" | tee "/opt/stack/status/stack/q-svc.failure"
/usr/local/bin/nova-api & echo $! >/opt/stack/status/stack/n-api.pid; fg || echo "n-api failed to start" | tee "/opt/stack/status/stack/n-api.failure"
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-obj.pid; fg || echo "n-obj failed to start" | tee "/opt/stack/status/stack/n-obj.failure"
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC & echo $! >/opt/stack/status/stack/n-novnc.pid; fg || echo "n-novnc failed to start" | tee "/opt/stack/status/stack/n-novnc.failure"
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini & echo $! >/opt/stack/status/stack/q-svc.pid; fg || echo "q-svc failed to start" | tee "/opt/stack/status/stack/q-svc.failure"
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini & echo $! >/opt/stack/status/stack/q-l3.pid; fg || echo "q-l3 failed to start" | tee "/opt/stack/status/stack/q-l3.failure"
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-cond.pid; fg || echo "n-cond failed to start" | tee "/opt/stack/status/stack/n-cond.failure"
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC & echo $! >/opt/stack/status/stack/n-novnc.pid; fg || echo "n-novnc failed to start" | tee "/opt/stack/status/stack/n-novnc.failure"
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-cond.pid; fg || echo "n-cond failed to start" | tee "/opt/stack/status/stack/n-cond.failure"
/opt/stack/cinder/bin/cinder-scheduler --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-sch.pid; fg || echo "c-sch failed to start" | tee "/opt/stack/status/stack/c-sch.failure"
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini & echo $! >/opt/stack/status/stack/q-l3.pid; fg || echo "q-l3 failed to start" | tee "/opt/stack/status/stack/q-l3.failure"
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-xvnc.pid; fg || echo "n-xvnc failed to start" | tee "/opt/stack/status/stack/n-xvnc.failure"
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-xvnc.pid; fg || echo "n-xvnc failed to start" | tee "/opt/stack/status/stack/n-xvnc.failure"
/usr/local/bin/glance-api --config-file=/etc/glance/glance-api.conf & echo $! >/opt/stack/status/stack/g-api.pid; fg || echo "g-api failed to start" | tee "/opt/stack/status/stack/g-api.failure"
sudo tail -f /var/log/apache2/horizon_error.log & echo $! >/opt/stack/status/stack/horizon.pid; fg || echo "horizon failed to start" | tee "/opt/stack/status/stack/horizon.failure"
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug & echo $! >/opt/stack/status/stack/key.pid; fg || echo "key failed to start" | tee "/opt/stack/status/stack/key.failure"
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini & echo $! >/opt/stack/status/stack/q-svc.pid; fg || echo "q-svc failed to start" | tee "/opt/stack/status/stack/q-svc.failure"
/usr/local/bin/glance-registry --config-file=/etc/glance/glance-registry.conf & echo $! >/opt/stack/status/stack/g-reg.pid; fg || echo "g-reg failed to start" | tee "/opt/stack/status/stack/g-reg.failure"
/opt/stack/heat/bin/heat-api-cfn --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-api-cfn.pid; fg || echo "h-api-cfn failed to start" | tee "/opt/stack/status/stack/h-api-cfn.failure"
/opt/stack/heat/bin/heat-api --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-api.pid; fg || echo "h-api failed to start" | tee "/opt/stack/status/stack/h-api.failure"
/opt/stack/heat/bin/heat-api-cloudwatch --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-api-cw.pid; fg || echo "h-api-cw failed to start" | tee "/opt/stack/status/stack/h-api-cw.failure"
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-xvnc.pid; fg || echo "n-xvnc failed to start" | tee "/opt/stack/status/stack/n-xvnc.failure"
cd /opt/devstack/
ls -la
./unstack.sh
vi local.conf 
./stack.sh
sudo reboot
/opt/stack/cinder/bin/cinder-api --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-api.pid; fg || echo "c-api failed to start" | tee "/opt/stack/status/stack/c-api.failure"
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC & echo $! >/opt/stack/status/stack/n-novnc.pid; fg || echo "n-novnc failed to start" | tee "/opt/stack/status/stack/n-novnc.failure"
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini & echo $! >/opt/stack/status/stack/q-svc.pid; fg || echo "q-svc failed to start" | tee "/opt/stack/status/stack/q-svc.failure"
python /usr/local/bin/neutron-openvswitch-agent --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini & echo $! >/opt/stack/status/stack/q-agt.pid; fg || echo "q-agt failed to start" | tee "/opt/stack/status/stack/q-agt.failure"
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-obj.pid; fg || echo "n-obj failed to start" | tee "/opt/stack/status/stack/n-obj.failure"
/opt/stack/cinder/bin/cinder-scheduler --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-sch.pid; fg || echo "c-sch failed to start" | tee "/opt/stack/status/stack/c-sch.failure"
/usr/local/bin/nova-api & echo $! >/opt/stack/status/stack/n-api.pid; fg || echo "n-api failed to start" | tee "/opt/stack/status/stack/n-api.failure"
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug & echo $! >/opt/stack/status/stack/key.pid; fg || echo "key failed to start" | tee "/opt/stack/status/stack/key.failure"
/opt/stack/cinder/bin/cinder-volume --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-vol.pid; fg || echo "c-vol failed to start" | tee "/opt/stack/status/stack/c-vol.failure"
/usr/local/bin/glance-api --config-file=/etc/glance/glance-api.conf & echo $! >/opt/stack/status/stack/g-api.pid; fg || echo "g-api failed to start" | tee "/opt/stack/status/stack/g-api.failure"
/opt/stack/heat/bin/heat-engine --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-eng.pid; fg || echo "h-eng failed to start" | tee "/opt/stack/status/stack/h-eng.failure"
/usr/local/bin/nova-consoleauth --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-cauth.pid; fg || echo "n-cauth failed to start" | tee "/opt/stack/status/stack/n-cauth.failure"
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-sch.pid; fg || echo "n-sch failed to start" | tee "/opt/stack/status/stack/n-sch.failure"
/usr/local/bin/nova-cert --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-crt.pid; fg || echo "n-crt failed to start" | tee "/opt/stack/status/stack/n-crt.failure"
python /usr/local/bin/neutron-metadata-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/metadata_agent.ini & echo $! >/opt/stack/status/stack/q-meta.pid; fg || echo "q-meta failed to start" | tee "/opt/stack/status/stack/q-meta.failure"
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini & echo $! >/opt/stack/status/stack/q-l3.pid; fg || echo "q-l3 failed to start" | tee "/opt/stack/status/stack/q-l3.failure"
python /usr/local/bin/neutron-openvswitch-agent --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-cond.pid; fg || echo "n-cond failed to start" | tee "/opt/stack/status/stack/n-cond.failure"
sg libvirtd '/usr/local/bin/nova-compute --config-file /etc/nova/nova.conf' & echo $! >/opt/stack/status/stack/n-cpu.pid; fg || echo "n-cpu failed to start" | tee "/opt/stack/status/stack/n-cpu.failure"
/opt/stack/heat/bin/heat-engine --config-file=/etc/heat/heat.conf & echo $! >/opt/stack/status/stack/h-eng.pid; fg || echo "h-eng failed to start" | tee "/opt/stack/status/stack/h-eng.failure"
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-sch.pid; fg || echo "n-sch failed to start" | tee "/opt/stack/status/stack/n-sch.failure"
/opt/stack/heat/bin/heat-api-cfn --config-file=/etc/heat/heat.conf
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf & echo $! >/opt/stack/status/stack/n-sch.pid; fg || echo "n-sch failed to start" | tee "/opt/stack/status/stack/n-sch.failure"
/opt/stack/heat/bin/heat-api --config-file=/etc/heat/heat.conf
sudo tail -f /var/log/apache2/horizon_error.log & echo $! >/opt/stack/status/stack/horizon.pid; fg || echo "horizon failed to start" | tee "/opt/stack/status/stack/horizon.failure"
/opt/stack/cinder/bin/cinder-volume --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-vol.pid; fg || echo "c-vol failed to start" | tee "/opt/stack/status/stack/c-vol.failure"
/opt/stack/cinder/bin/cinder-volume --config-file /etc/cinder/cinder.conf & echo $! >/opt/stack/status/stack/c-vol.pid; fg || echo "c-vol failed to start" | tee "/opt/stack/status/stack/c-vol.failure"
vi /etc/nova/nova.conf 
ls -la
sudo /opt/devstack/rejoin-stack.sh
/opt/stack/cinder/bin/cinder-scheduler --config-file /etc/cinder/cinder.conf
/opt/stack/cinder/bin/cinder-api --config-file /etc/cinder/cinder.conf
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf
/usr/local/bin/nova-consoleauth --config-file /etc/nova/nova.conf
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC
/usr/local/bin/nova-cert --config-file /etc/nova/nova.conf
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf
/usr/local/bin/nova-compute --config-file /etc/nova/nova.conf
python /usr/local/bin/neutron-metadata-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/metadata_agent.ini
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini
python /usr/local/bin/neutron-dhcp-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/dhcp_agent.ini
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/usr/local/bin/nova-api
/usr/local/bin/glance-api --config-file=/etc/glance/glance-api.conf
/usr/local/bin/glance-registry --config-file=/etc/glance/glance-registry.conf
sudo tail -f /var/log/apache2/horizon_error.log
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug
cd /opt/devstack/
vi rejoin-stack.sh 
sudo sudo iptables -t nat -A POSTROUTING -o eth0 MASQUERADE
sudo sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
vi rejoin-stack.sh 
ls -la
cp /etc/nova/nova.conf ./
vi nova.conf 
cp nova.conf /etc/nova/
sudo shutdown -h now
python /usr/local/bin/neutron-openvswitch-agent --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
ifconfig -a
sudo /opt/devstack/rejoin-stack.sh
/opt/stack/heat/bin/heat-api-cloudwatch --config-file=/etc/heat/heat.conf
/opt/stack/heat/bin/heat-api-cfn --config-file=/etc/heat/heat.conf
/opt/stack/heat/bin/heat-api --config-file=/etc/heat/heat.conf
/opt/stack/heat/bin/heat-engine --config-file=/etc/heat/heat.conf
/opt/stack/cinder/bin/cinder-volume --config-file /etc/cinder/cinder.conf
/opt/stack/cinder/bin/cinder-scheduler --config-file /etc/cinder/cinder.conf
/opt/stack/cinder/bin/cinder-api --config-file /etc/cinder/cinder.conf
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf
/usr/local/bin/nova-consoleauth --config-file /etc/nova/nova.conf
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf
/usr/local/bin/nova-cert --config-file /etc/nova/nova.conf
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf
python /usr/local/bin/neutron-metadata-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/metadata_agent.ini
/usr/local/bin/nova-compute --config-file /etc/nova/nova.conf
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini
python /usr/local/bin/neutron-dhcp-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/dhcp_agent.ini
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/usr/local/bin/nova-api
/usr/local/bin/glance-api --config-file=/etc/glance/glance-api.conf
/usr/local/bin/glance-registry --config-file=/etc/glance/glance-registry.conf
sudo tail -f /var/log/apache2/horizon_error.log
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug
cd /opt/devstack/
ls -la
source openrc admin demo
cinder list
cinder force-delete 9058d69c-3b9d-4357-b261-754640c8172c 
cd ..
cd stack
ls -la
find . -name strutils.py
vi ./cinder/cinder/openstack/common/strutils.py
sudo shutdown -h now
python /usr/local/bin/neutron-openvswitch-agent --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/opt/stack/heat/bin/heat-api-cloudwatch --config-file=/etc/heat/heat.conf
/opt/stack/heat/bin/heat-api --config-file=/etc/heat/heat.conf
/opt/stack/heat/bin/heat-api-cfn --config-file=/etc/heat/heat.conf
/opt/stack/heat/bin/heat-engine --config-file=/etc/heat/heat.conf
/opt/stack/cinder/bin/cinder-scheduler --config-file /etc/cinder/cinder.conf
/opt/stack/cinder/bin/cinder-api --config-file /etc/cinder/cinder.conf
/opt/stack/cinder/bin/cinder-volume --config-file /etc/cinder/cinder.conf
sudo /opt/devstack/rejoin-stack.sh
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf
/usr/local/bin/nova-consoleauth --config-file /etc/nova/nova.conf
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf
/usr/local/bin/nova-cert --config-file /etc/nova/nova.conf
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf
/usr/local/bin/nova-compute --config-file /etc/nova/nova.conf
python /usr/local/bin/neutron-metadata-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/metadata_agent.ini
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini
python /usr/local/bin/neutron-dhcp-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/dhcp_agent.ini
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/usr/local/bin/nova-api
/usr/local/bin/glance-api --config-file=/etc/glance/glance-api.conf
/usr/local/bin/glance-registry --config-file=/etc/glance/glance-registry.conf
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug
ls -la
df -h
cd /opt
ls -la
cd stack/
ls -la
cd data
ls -la
du -h
ifconfig -a
ls -la
gzip stack-volumes-backing-file
ls -la
df -h
du -h
cd glance/
ls -la
cd cache/
ls -la
cd ..
ls -la
cd ..
ls -la
sudo shutdown -h now
sudo -i -u stack
cd /opt/
ls -la
cd devstack/
ls -la
source openrc admin demo
cinder list
cinder force-delete 9058d69c-3b9d-4357-b261-754640c8172c
cinder force-delete be69d132-8ee3-4c70-9e2c-dd519cbeaedb 
shutdown -h now
sudo shutdown -h now
python /usr/local/bin/neutron-openvswitch-agent --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/opt/stack/heat/bin/heat-api-cloudwatch --config-file=/etc/heat/heat.conf
/opt/stack/heat/bin/heat-api-cfn --config-file=/etc/heat/heat.conf
/opt/stack/heat/bin/heat-api --config-file=/etc/heat/heat.conf
/opt/stack/heat/bin/heat-engine --config-file=/etc/heat/heat.conf
/opt/stack/cinder/bin/cinder-volume --config-file /etc/cinder/cinder.conf
/opt/stack/cinder/bin/cinder-scheduler --config-file /etc/cinder/cinder.conf
/opt/stack/cinder/bin/cinder-api --config-file /etc/cinder/cinder.conf
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf
/usr/local/bin/nova-consoleauth --config-file /etc/nova/nova.conf
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf
/usr/local/bin/nova-cert --config-file /etc/nova/nova.conf
/usr/local/bin/nova-compute --config-file /etc/nova/nova.conf
python /usr/local/bin/neutron-metadata-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/metadata_agent.ini
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini
python /usr/local/bin/neutron-dhcp-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/dhcp_agent.ini
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/usr/local/bin/nova-api
/usr/local/bin/glance-api --config-file=/etc/glance/glance-api.conf
/usr/local/bin/glance-registry --config-file=/etc/glance/glance-registry.conf
sudo tail -f /var/log/apache2/horizon_error.log
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug
sudo /opt/devstack/rejoin-stack.sh
df -h
cd /opt/
ls -la
cd devstack/
ls -la
more local.conf 
ls -la
exit
python /usr/local/bin/neutron-openvswitch-agent --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/opt/stack/heat/bin/heat-api-cloudwatch --config-file=/etc/heat/heat.conf
sudo /opt/devstack/rejoin-stack.sh
/opt/stack/heat/bin/heat-engine --config-file=/etc/heat/heat.conf
/opt/stack/cinder/bin/cinder-volume --config-file /etc/cinder/cinder.conf
/opt/stack/cinder/bin/cinder-scheduler --config-file /etc/cinder/cinder.conf
/opt/stack/cinder/bin/cinder-api --config-file /etc/cinder/cinder.conf
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf
/usr/local/bin/nova-consoleauth --config-file /etc/nova/nova.conf
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf
/usr/local/bin/nova-novncproxy --config-file /etc/nova/nova.conf --web /opt/stack/noVNC
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf
/usr/local/bin/nova-cert --config-file /etc/nova/nova.conf
/usr/local/bin/nova-conductor --config-file /etc/nova/nova.conf
/usr/local/bin/nova-compute --config-file /etc/nova/nova.conf
python /usr/local/bin/neutron-metadata-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/metadata_agent.ini
python /usr/local/bin/neutron-l3-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/l3_agent.ini
python /usr/local/bin/neutron-dhcp-agent --config-file /etc/neutron/neutron.conf --config-file=/etc/neutron/dhcp_agent.ini
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/usr/local/bin/nova-api
/usr/local/bin/glance-api --config-file=/etc/glance/glance-api.conf
/usr/local/bin/glance-registry --config-file=/etc/glance/glance-registry.conf
sudo tail -f /var/log/apache2/horizon_error.log
/opt/stack/keystone/bin/keystone-all --config-file /etc/keystone/keystone.conf --debug
cd /opt/devstack/
cd .
cd ..
cd stack/
ls -la
cd data
ls -la
gzip stack-volumes-backing-file
du -h
cd ..
ls -la
sudo shutdown -h now
/usr/local/bin/nova-compute --config-file /etc/nova/nova.conf
ls -la
cd /
ls -la
cd /opt
ls -la
du -h
ls -la
exit
/opt/stack/heat/bin/heat-engine --config-file=/etc/heat/heat.conf
exit
sudo /opt/devstack/rejoin-stack.sh 
python /usr/local/bin/neutron-openvswitch-agent --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/opt/stack/heat/bin/heat-api-cfn --config-file=/etc/heat/heat.conf
reboot
/opt/stack/cinder/bin/cinder-scheduler --config-file /etc/cinder/cinder.conf
/opt/stack/cinder/bin/cinder-api --config-file /etc/cinder/cinder.conf
/usr/local/bin/nova-objectstore --config-file /etc/nova/nova.conf
/usr/local/bin/nova-consoleauth --config-file /etc/nova/nova.conf
/usr/local/bin/nova-xvpvncproxy --config-file /etc/nova/nova.conf
/usr/local/bin/nova-scheduler --config-file /etc/nova/nova.conf
python /usr/local/bin/neutron-server --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini
/usr/local/bin/glance-api --config-file=/etc/glance/glance-api.conf
/usr/local/bin/nova-cert --config-file /etc/nova/nova.conf
sudo tail -f /var/log/apache2/horizon_error.log
